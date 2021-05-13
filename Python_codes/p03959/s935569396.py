import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Ts = list(mapint())
As = list(mapint())
mod = 10**9 + 7

maxi = [10**18]*N
confirmed = [-1]*N

now = 0
for i in range(N):
    t = Ts[i]
    if t>now:
        now = t
        confirmed[i] = t
    else:
        maxi[i] = t

now = 0
for i in range(N-1, -1, -1):
    a = As[i]
    if a>now:
        now = a
        if maxi[i]<a:
            print(0)
            exit()          
        if confirmed[i]==-1:
            confirmed[i] = a
        elif confirmed[i]!=a:
            print(0)
            exit()
    else:
        maxi[i] = min(maxi[i], a)

ans = 1
for i in range(N):
    if confirmed[i]!=-1:
        continue
    ans *= maxi[i]
    ans %= mod

print(ans)