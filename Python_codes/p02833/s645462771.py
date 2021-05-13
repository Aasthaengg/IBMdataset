N = int(input())

if N < 2 or N % 2 == 1:
  print(0)
  exit()
  
res = 0

de = 10
while de < N + 1:
  res += N // de
  de *= 5
print(res)