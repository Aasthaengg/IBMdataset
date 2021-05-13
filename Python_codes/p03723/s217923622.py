a, b, c = [int(i) for i in input().split()]

cnt = 0
history = set()
while True:
  if (a, b, c) in history:
    print(-1)
    exit(0)
  if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
    print(cnt)
    exit(0)
  a, b, c = sorted([a, b, c])
  history.add((a, b, c))
  na = b // 2 + c // 2
  nb = a // 2 + c // 2
  nc = a // 2 + b // 2
  a = na
  b = nb 
  c = nc
  cnt += 1