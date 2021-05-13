k, x = map(int, input().split())
ans = [i for i in range(x - k + 1, x + k) if -1000000 <= i <= 1000000]
for e in ans:
  print(e, end=' ')