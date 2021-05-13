import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, H, W = mapint()
cnt = 0
for _ in range(N):
    a, b = mapint()
    if a>=H and b>=W:
        cnt += 1
    else:
        continue
print(cnt)