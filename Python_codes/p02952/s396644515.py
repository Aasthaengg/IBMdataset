n = int(input())
i = 5
while True:
  if (n//(10**i) != 0):
    break
  i = i - 1
i = i + 1

if (i%2 == 0):
  i = i//2
  ans = 0
  for j in range(i):
    ans = ans + 9*10**(2*j)
  print(ans)
else:
  i2 = (i - 1)//2
  ans = 0
  for j in range(i2):
    ans = ans + 9*10**(2*j)
  tmp = 0
  for j in range(i - 1):
    tmp = tmp + 9*(10**j)
  ans = ans + n - tmp
  print(ans)
