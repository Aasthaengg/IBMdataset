import math
N = int(input())
lst = [True]*(N*2)
for i in range(2,int(math.sqrt(N*2))+1):
  for j in range(i+i,N*2,i):
    lst[j] = False
for i in range(N,len(lst)):
  if lst[i]:
    print(i)
    break