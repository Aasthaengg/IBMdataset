r,g,b,n = map(int, input().split())
ans = 0
rgb = sorted([r,g,b])
n_rgb = []
for e in rgb:
  n_rgb.append(n//e)
for i in range(n_rgb[2]+1):
  N2 = n-i*rgb[2]
  for j in range(n_rgb[1]+1):
    N = N2 - j*rgb[1]
    if  N>=0 and N%rgb[0]==0:
      ans+=1
      
print(ans)