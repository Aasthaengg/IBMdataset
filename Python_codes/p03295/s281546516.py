import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for m in range(M)]

ab.sort(key= lambda x: x[1])
removed = -1
ans = 0

for a, b in ab:
  if a > removed:
    removed = b - 1
    ans += 1

print(ans)