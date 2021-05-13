N = int(input())
PX = PY = PT = 0

for _ in range(N):
  T,X,Y = map(int,input().split())
  if abs(X-PX)+abs(Y-PY)>T-PT or (X+Y-PX-PY)%2 != (T-PT)%2:
    print("No")
    exit()
  else:
    PX = X
    PY = Y
    PT = T
    
print("Yes")