a = int(input())
b = int(input())
h = int(input())

s = 0
if 1 <= a <= 100 and 1 <= b <= 100 and 1 <= h <= 100 and h % 2 == 0:
  s = (a + b) * h / 2
  print(int(s))