n = input()
ans = 0
if 1 <= int(n[0:2]) <= 12 and 0 <= int(n[2:4]) <= 99:
  ans += 1
if 0 <= int(n[0:2]) <= 99 and 1 <= int(n[2:4]) <= 12:
  ans += 3
if ans == 1:
  print('MMYY')
elif ans == 3:
  print('YYMM')
elif ans == 4:
  print('AMBIGUOUS')
else:
  print('NA')