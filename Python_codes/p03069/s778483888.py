import sys
input = sys.stdin.readline
N = int(input())
s = list(input())[: -1]
cs = [0] * (N + 1)
for i in range(N): cs[i + 1] = cs[i] + (s[i] == "#")
res = float("inf")
for i in range(N + 1):
  r = cs[-1] - cs[i]
  l = i - cs[i]
  res = min(res, N - i - r + i - l)
print(res)