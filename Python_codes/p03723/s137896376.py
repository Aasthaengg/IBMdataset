X=[int(x) for x in input().split()]
count=0
if ((X[0]%2-1)*(X[1]%2-1)*(X[2]%2-1)!=0 and X[0]==X[1] and X[1]==X[2]):
  count=-1
else:
  while((X[0]%2-1)*(X[1]%2-1)*(X[2]%2-1)!=0):
    Y=[0,0,0]
    Y[0]=(X[1]+X[2])/2
    Y[1]=(X[0]+X[2])/2
    Y[2]=(X[1]+X[0])/2
    X=Y
    count =count+1
print(count) 