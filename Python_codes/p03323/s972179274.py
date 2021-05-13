a, b = map(int, input().split())

if a > 8 or b > 8:
  print(':(')
elif a <= 8 and b <= 8:
  print('Yay!')