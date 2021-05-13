n = int(input())

num =[[[0 for i in range(10)] for i in range(3)] for i in range(4)]

for i in range(n):
  b,f,r,v = map(int, input().split())
  num[b-1][f-1][r-1] += v

x = 0

for i in range(4):
  if x!=0:
    print('#'*20)
  x += 1
  
  for b in range(3):
    for f in range(10):
      print(' %d'%(num[i][b][f]), end ='')
    print()
