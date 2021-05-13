N, Y = map(int, input().split())
Y //= 1000
i = 0
f = 0
while 1:
  if 10 * i > Y:
    break
  y = Y - 10 * i
  n = N - i
  if n <= y <=  5 * n and (y - n) % 4 == 0:
    print(str(i) + " " + str((y-n)//4) + " " + str((5 * n - y) // 4))
    f = 1
    break
  i += 1
if f == 0:
  print("-1 -1 -1")