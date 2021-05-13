#00:58
n,u = map(int,input().split())
wv = [[] for _ in range(4)]
for i in range(n):
  w,v = map(int,input().split())
  if i == 0:
    w0 = w
  wv[w-w0].append(v)
#print(wv)
z = []
for d in range(4):
  wv[d].sort(reverse=True)
  z.append(len(wv[d]))
cum = []
for d in range(4):
  tmp = [0]
  for x in wv[d]:
    tmp.append(tmp[-1]+x)
  cum.append(tmp)
#print(cum)
#print(z)
can = [0]
for i0 in range(z[0]+1):
  y0 = cum[0][i0]
  for i1 in range(z[1]+1):
    y1 = cum[1][i1]
    for i2 in range(z[2]+1):
      y2 = cum[2][i2]
      for i3 in range(z[3]+1):
        y3 = cum[3][i3]
        if i0*w0 + i1*(w0+1) + i2*(w0+2) + i3*(w0+3) <= u:
          can.append(y0+y1+y2+y3)
#print(can)
print(max(can))