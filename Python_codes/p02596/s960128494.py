k = int(input())
mo = 7
mo = mo % k
for i in range(1 , k + 1):
  if mo == 0:
    print(i)
    break
  if mo != 0:
    mo = (mo * 10 + 7) % k
else:
  print(-1)