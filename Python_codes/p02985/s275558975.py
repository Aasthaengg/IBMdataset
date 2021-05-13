from collections import deque
import sys

N, K = map(int, input().split())
mod = 10**9+7

T = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    T[a-1].append(b-1)
    T[b-1].append(a-1)

fac = [0]*(K+1)
fac[0] = 1
fac[1] = 1
for i in range(2, K+1):
    fac[i] = fac[i-1] * i % mod

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

if K - len(T[0]) - 1 < 0:
    print(0)
    sys.exit()

ans = fac[K] * modinv(fac[K - len(T[0]) - 1])
q = deque(T[0])
used = [0]*N
used[0] = 1
for i in T[0]:
    used[i] = 1

while(len(q)>0):
    a = q.popleft()
    if len(T[a]) != 1:
        if K - len(T[a]) - 1 < 0:
            print(0)
            sys.exit()
        ans *= fac[K-2]*modinv(fac[K - len(T[a]) - 1])
        ans %= mod
    for i in T[a]:
        if used[i] == 0:
            q.append(i)
            used[i] = 1
print(ans%mod)