import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
red = N-K
mod = 10**9+7

pos = [1]*(N+1)
neg = [1]*(N+1)
s = 1
for i in range(1, N+1):
    s *= i
    s %= mod
    pos[i] = s
    neg[i] = pow(s, mod-2, mod)

# val = 0
# for i in range(1, K+1):
#     now = (pos[red+i]*neg[red]*neg[i]-val)*pos[K-1]*neg[i-1]*neg[K-i]%mod
#     print(now)
#     val = (now + val)%mod

for i in range(1, K+1):
    if N+1<K+i:
        print(0)
        continue
    ans = pos[red+1]*neg[i]*neg[red+1-i]*pos[K-1]*neg[i-1]*neg[K-i]
    print(ans%mod)