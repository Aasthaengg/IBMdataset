month1, day1 = map(int, input().rstrip().split(' '))
month2, day2 = map(int, input().rstrip().split(' '))

if day1 > day2:
  print(1)
else:
  print(0)
