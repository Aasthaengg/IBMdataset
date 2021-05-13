N = int(input())
t,x,y = 0,0,0
for n in range(N):
  T,X,Y = map(int,input().split())
  D = abs(X-x) + abs(Y - y) 
  if D <= T - t and (T - t - D) % 2 == 0:
    x = X
    y = Y
    t = T
  else:
    print('No')
    break
else:
  print('Yes')
