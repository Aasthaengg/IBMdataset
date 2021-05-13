K, X = map(int, input().split())
left = X-K+1
right = X+K
for i in range(left, right):
  print(i, end=" ")