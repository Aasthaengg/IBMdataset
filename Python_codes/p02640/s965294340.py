X,Y = map(int,input().split())
for a in range(X+1):
  b = X - a
  if b >= 0 and a*2 + b*4 == Y:
    print('Yes')
    exit()
print('No')