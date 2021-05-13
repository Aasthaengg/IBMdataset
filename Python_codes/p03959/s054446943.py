n = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))

ans = 1
mod = 10**9 + 7
inf = float('inf')

for i in range(n-1):
    if A[i] == A[i+1]:
        A[i] = -A[i]
    if T[n-i-1] == T[n-i-2]:
        T[n-i-1] = -T[n-i-1]

for t,a in zip(T,A):
    if t < 0 and a < 0:
        ans *= min(-t,-a)
        ans %= mod
    elif t < 0:
        if -t < a:
            ans *= 0
    elif a < 0:
        if -a < t:
            ans *= 0
    elif t != a:
        ans *= 0
print(ans)
