n, k = map(int, input().split())
l = (n-1)*(n-2)//2
d = l-k
if d < 0:
  print(-1)
else:
  m = n-1+d
  print(m)
  A = [(i, j) for i in range(1, n) for j in range(i+1, n+1)]
  for i in range(m):
    print(*A[i])