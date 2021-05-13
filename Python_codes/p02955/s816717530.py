N,K = map(int,input().split())
A = list(map(int,input().split()))
s = sum(A)

divisors = []
for i in range(1,int(s**0.5)+1):
    if s%i==0:
        divisors.append(i)
        divisors.append(s//i)
divisors = list(set(divisors))
divisors.sort(reverse=True)

def possible(n):
    a = []
    for i in range(N):
        if A[i]%n != 0:
            a.append(A[i]%n)
    a.sort()
    k = 0
    while k <= K and a:
        m = a[0]
        M = a[-1]
        if m <= n-M:
            k += m
            a[-1] = (M+m)%n
            a[0] = 0
        else:
            k += n-M
            a[0] = (m-n+M)%n
            a[-1] = 0
        if a[0]==0:
            a = a[1:]
        if a[-1]==0:
            a = a[:-1]
        a.sort()
    return k<=K

for n in divisors:
    if possible(n):
        ans = n
        break

print(ans)