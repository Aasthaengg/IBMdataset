n = int(input())
a = list(map(int, input().split()))
if n == 1:
  print(0)
else:
  before = a[0]
  cnt = 0
  ans = 0
  for i in range(1, n):
    if a[i] == before:
      cnt += 1
    else:
      ans += (cnt + 1) // 2
      cnt = 0
    before = a[i]
  ans += (cnt + 1) // 2
  print(ans)
