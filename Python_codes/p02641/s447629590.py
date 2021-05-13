X, N = map(int, input().split())
if N == 0:
  print(X)
else:
  nums = list(map(int, input().split()))
  existed = [0 for _ in range(102)]
  for num in nums:
    existed[num] = 1
  for d in range(101):
    if 0 <= X-d <= 101 and existed[X-d] == 0:
      print(X-d)
      exit()
    if 0 <= X+d <= 101 and existed[X+d] == 0:
      print(X+d)
      exit()