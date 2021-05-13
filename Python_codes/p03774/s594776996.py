N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
c=[list(map(int,input().split())) for _ in range(M)]
for i in range(N):
  p,q=0,10**9
  for j in range(M):
    if q>abs(c[j][0]-a[i][0])+abs(c[j][1]-a[i][1]):
      q=abs(c[j][0]-a[i][0])+abs(c[j][1]-a[i][1])
      p=j+1
    elif q==abs(c[j][0]-a[i][0])+abs(c[j][1]-a[i][1]):
      if abs(p-i)>abs(j+1-i):
        p=j+1
  print(p)