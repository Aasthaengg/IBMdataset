a, b = map(int, input().split())
s = a+b
k = s/2 - s//2

if k > 0.4:
  print(s//2+1)
else:
  print(s//2)