import sys
input = sys.stdin.readline
N, H = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(N)]
a.sort(key = lambda x: -x[1])
cs = [0] * (N + 1)
mx = 0
for i in range(N):
  cs[i + 1] = cs[i] + a[i][1]
  mx = max(mx, a[i][0])
res = H + 1
for i in range(N + 1): res = min(res, -(-max(0, H - cs[i]) // mx) + i)
print(res)