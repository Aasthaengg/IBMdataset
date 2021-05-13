X=[0]*4
for i in range(3):
  A,B=map(int,input().split())
  X[A-1]+=1
  X[B-1]+=1
X.sort()
if(X[0]==1 and X[1]==1 and X[2]==2):
  print("YES")
else:
  print("NO")