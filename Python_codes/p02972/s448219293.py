N = int(input())
A = list(map(int,input().split()))

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

B = [0]*N
for i in range(N):
    X = N-i
    P = B[X-1]
    Q = A[X-1]
    if P==Q:
        B[X-1] = 0
    else:
        XDL = make_divisors(X)
        for XD in XDL:
            if XD==X:
                B[XD-1] = 1
            else:
                B[XD-1] = 1 - B[XD-1]
out = []
cnt = 0
for i in range(N):
    if B[i]==1:
        out.append(i+1)
        cnt+=1
print(cnt)
if len(out)>0:
    print(*out)