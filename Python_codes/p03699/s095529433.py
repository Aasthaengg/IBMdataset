n = int(input())
s = sorted([int(input()) for _ in range(n)])

sumNum = sum(s)
if sumNum % 10 != 0:
  print(sumNum)
  exit()
else:
  ans = 0
  for i in s:
    if (sumNum - i) % 10 != 0:
      ans = max(ans, sumNum - i)
  print(ans)