mod = 10**9+7
N = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))
Tmax = (0,-1)
Amax = (0,-1)
h = [0]*N
not_confirmed = [True]*N
for i in range(N):
    if Tmax[0] < T[i]:
        Tmax = (T[i],i)
        not_confirmed[i] = False
    if Amax[0] < A[N-1-i]:
        Amax = (A[N-1-i],N-1-i)
        not_confirmed[N-1-i] = False
    h[i] = min(T[i],A[i])
if (Amax[1] < Tmax[1]) or (Tmax[0] != Amax[0]):
    print(0)
    exit()

ans = 1
for i in range(N):
    ans *= h[i] if not_confirmed[i] else 1
    ans %= mod
print(ans)