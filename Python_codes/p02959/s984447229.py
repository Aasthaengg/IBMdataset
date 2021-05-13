N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
tot = 0
c = 0
for i in range(N):
    a = A[i]
    b = B[i]
    if a>=c:
        a -= c
        tot += c
        if a>=b:
            tot += b
            c = 0
        else:
            tot += a
            c = b-a
    else:
        tot += a
        c = b
a = A[N]
tot += min(a,c)
print(tot)