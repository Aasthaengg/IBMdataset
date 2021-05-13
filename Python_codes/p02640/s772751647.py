X,Y = map(int,input().split())
count = 0
for i in range(X+1):
  for j in range(X+1):
    if 2*i + 4*j == Y and i+j ==X:
      count +=1
if count == 0:
  print('No')
else:
  print('Yes')