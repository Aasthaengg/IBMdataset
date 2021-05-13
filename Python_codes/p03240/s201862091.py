n = int(input())
hist = [tuple(map(int,input().split())) for _ in range(n)]
hist.sort(key=lambda x: x[2], reverse=1)

cands = []
x0,y0,h0 = hist[0]

for i in range(0,101):
  for j in range(0,101):
    if h0 == 0:
      cands.append((i,j,1))
    else:
      cands.append((i,j, h0+abs(i-x0)+abs(j-y0)))
    
for X,Y,H in cands:
  for x,y,h in hist:
    if max(H-abs(X-x)-abs(Y-y),0) == h:
      continue
    else:
      break
  else:
    print(X,Y,H)
    break
    

