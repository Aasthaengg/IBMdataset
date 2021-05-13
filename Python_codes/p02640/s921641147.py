X,Y = map(int,input().split())
Max = X*4
while Max >= X*2:
  if Max == Y:
    print('Yes')
    exit()
  Max -= 2
print('No')