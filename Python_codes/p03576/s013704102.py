N, K = map(int, input().split())
ls = []
for i in range(N):
  x, y = map(int, input().split())
  ls += [(x,y)]
m = -1
for i in range(N):
  for j in range(i+1,N):
    for p in range(N):
      for q in range(p+1,N):
        
        x1, y1 = ls[i]
        x2, y2 = ls[j]
        x3, y3 = ls[p]
        x4, y4 = ls[q]
        cnt = 0
        flag = False
        X1 = min(x1, x2)
        X2 = max(x1, x2)
        Y1 = min(y3, y4)
        Y2 = max(y3, y4)
        for a in range(N):
          x, y = ls[a]
          """
          print('"""""""')
          print(cnt)
          print(X1,X2,x)
          print(Y1,Y2,y)
          """
          if X1<=x<=X2 and Y1<=y<=Y2:
            cnt += 1
          if cnt>=K:
            n = (X2-X1)*(Y2-Y1)
            if m==-1 or n<m:
              m = n
            break
print(m)