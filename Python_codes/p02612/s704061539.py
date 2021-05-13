N = int(input())

s = N // 1000
t = N % 1000

pay = 0
dif = 0

if t != 0:
  pay = 1000 * (s + 1)
  dif = pay - N
  print(dif)
  
else:
  print(0)