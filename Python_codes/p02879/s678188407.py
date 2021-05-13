a,b = [int(a) for a in input().split()]
if a>9 or b>9:
  print(-1)
elif 1<=a<=9 and 1<=b<=9:
  print(a*b)