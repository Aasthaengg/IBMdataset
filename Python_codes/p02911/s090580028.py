n, k, q = map(int, input().split())
point = [0] * (n+1)
for _ in range(q):
  a = int(input())
  point[a] += 1

for i in range(1, n+1):
  if k + point[i] > q:
    print('Yes')
  else:
    print('No')
