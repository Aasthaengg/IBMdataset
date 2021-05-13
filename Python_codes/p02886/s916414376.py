import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Ds = list(mapint())

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        ans += Ds[i]*Ds[j]

print(ans)