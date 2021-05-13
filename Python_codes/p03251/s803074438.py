N,M,X,Y=list(map(int, input().split()))
xc=list(map(int, input().split()))
xc.append(X)
yc=list(map(int, input().split()))
yc.append(Y)
xc.sort()
yc.sort()
if xc[-1]>=yc[0]:
  print('War')
else:
  print('No War')