N,K = map(int, input().split())
P = []
for _ in range(N):
  a,b = map(int, input().split())
  P.append((a,b))
  
ans = 5 * 10 ** 18

def solve(xl,xr,yl,yr):
  xm, xM = min(xl[0], xr[0]), max(xl[0], xr[0])
  ym, yM = min(yl[1], yr[1]), max(yl[1], yr[1])
  cnt = 0
  for k in range(N):
    p,q = P[k]
    if xm <= p <= xM and ym <= q <= yM:
      cnt += 1
  #print(xm, xM, ym, yM, cnt)
  return cnt >= K
    
def calc(xl,xr,yl,yr):
  return abs(xr[0] - xl[0]) * abs(yr[1] - yl[1])
  
for i in range(N):
  for j in range(i+1,N):
    for k in range(N):
      for l in range(k+1,N):
        if solve(P[i], P[j], P[k], P[l]):
          wk = calc(P[i], P[j], P[k], P[l])
          #rint(i,j,k,l,wk)
          ans = min(ans, wk)
      
print(ans)