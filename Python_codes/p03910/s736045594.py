from math import ceil

N = int(input())
n = ceil((-1 + (1+8*N)**(1/2))/2)
d = n*(n+1)/2 - N
for i in range(1, n+1):
  if i != d:
    print(i)