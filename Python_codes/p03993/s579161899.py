import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
res = 0
for x in range(N):
  y = a[x]
  if x + 1 == a[y - 1]: res += 1
print(res // 2)