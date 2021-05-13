N,M,X,Y=map(int,input().split())
ListX = list(map(int, input().split()))
ListY = list(map(int, input().split()))
ListX.sort()
ListY.sort()
threX = max(X,ListX[N-1])
threY = min(Y,ListY[0])
Z = threX+1
if threY >= Z:
  print("No War")
else:
  print("War")