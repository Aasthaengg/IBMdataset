import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Hs = list(mapint())

ans = 0
tmp = 0
for i in range(1, N):
    if Hs[i]<=Hs[i-1]:
        tmp += 1
    else:
        ans = max(tmp, ans)
        tmp = 0
else:
    ans = max(tmp, ans)
print(ans)