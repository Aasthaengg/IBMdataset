import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Ps = list(mapint())
ans = 0

for i in range(1, N-1):
    if Ps[i-1]<=Ps[i]<Ps[i+1] or Ps[i+1]<=Ps[i]<Ps[i-1]:
        ans += 1
print(ans)