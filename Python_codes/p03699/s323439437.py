import sys
n = int(input())
s = [int(input()) for i in range(n)]
s = sorted(s)
if sum(s) % 10 != 0:
  print(sum(s))
  sys.exit()
elif all([ss % 10 == 0 for ss in s]):
  print(0)
  sys.exit()
else:
  for i in s:
    if (sum(s) - i) % 10 != 0:
      print(sum(s) - i)
      sys.exit()
