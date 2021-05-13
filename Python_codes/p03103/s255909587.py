import numpy as np
N,M = map(int, input().split())
AB = []
for i in range(N):
  tmp = list(map(int, input().split()))
  AB.append(tmp)
AB.sort()

count = 0
total_price = 0
i = 0
while count < M:
  total_price += AB[i][0]*AB[i][1]
  count += AB[i][1]
  i += 1
  if i == N:
    break

if count == M:
  print(int(total_price))
else:
  print(int(total_price-(count-M)*AB[i-1][0]))
  
  
