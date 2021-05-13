n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

if n <= k:
  print(0)
  exit(0)

for i in range(1, k+1):
  h[-i] = 0
print(sum(h))