D,N=map(int,input().split())
if D == 0:
  count=0
  for i in range(1,1000):
    if i % 100 != 0:
      count += 1
    if count == N:
      print(i)
      exit()
if D == 1:
  count = 0
  for i in range(100,1000000,100):
    if i % 10000 != 0:
      count += 1
    if count == N:
      print(i)
      exit()
if D == 2:
  count = 0
  for i in range(10000,10000*10000,10000):
    if i % 1000000 != 0:
      count += 1
    if count == N:
      print(i)
      exit()