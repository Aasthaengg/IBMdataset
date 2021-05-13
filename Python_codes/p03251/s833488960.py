import sys
n,m,X,Y=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))

d=min(y)-max(x)
warFlag = False
if d<=0:
    print("War")
    sys.exit()
else:
    for i in range(1, Y - X + 1):
        Z=X+i
        if (max(x)>=Z or min(y)<Z):
          warFlag = True
        else: #max(x) < Z, max(y) >= Z
          warFlag = False
          break
if warFlag:
  print("War")
else:
  print("No War")