import sys
input = sys.stdin.readline
N, K = map(int, input().split())
t = [0] * K
for i in range(1, N + 1): t[i % K] += 1
#print(t)
res = 0
for a in range(K):
  b = (K - a) % K
  c = (K - b) % K
  if (c + a) % K == 0:
    res += t[a] * t[b] * t[c]
print(res)