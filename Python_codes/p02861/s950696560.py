import math
import itertools
N = int(input())
X = []
Y = []
num = []
for i in range(N):
  x,y = map(int,input().split())
  X.append(x)
  Y.append(y)
  num.append(i)
p = itertools.permutations(num, N)
count_sum = 0
for i in p:
  count=0
  for j,k in enumerate(i):
    if j<N-1:
      count+=math.sqrt((X[k]-X[i[j+1]])**2+(Y[k]-Y[i[j+1]])**2)
  count_sum+=count
      
print(count_sum/math.factorial(N)) 
