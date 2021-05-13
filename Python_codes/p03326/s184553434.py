n,m = map(int,input().split())
xyz = [tuple(map(int,input().split())) for i in range(n)]
ma = 0
for i in range(-1,2,2):
  for j in range(-1,2,2):
    for k in range(-1,2,2):
      c = 0
      sx = sorted(xyz,key=lambda x:i*x[0]+j*x[1]+k*x[2],reverse=1)
      for l in range(m):
        c += i*sx[l][0]+j*sx[l][1]+k*sx[l][2]
      ma = max(ma,c)
print(ma)