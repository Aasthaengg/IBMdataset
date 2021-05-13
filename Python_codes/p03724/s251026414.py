import sys
input = sys.stdin.readline
N, M = map(int, input().split())
table = [0] * (N + 1)
for _ in range(M):
  u, v = map(int, input().split())
  table[u] += 1
  table[v] += 1

for i in range(N + 1):
  if table[i] % 2:
    print("NO")
    exit(0)
print("YES")