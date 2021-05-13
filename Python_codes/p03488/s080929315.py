s = list(map(len,input().split("T")))
x = s[::2]
y = s[1::2]
gx,gy = map(int,input().split())
if sum(x) < abs(gx) or sum(y) < abs(gy):
  print("No")
  exit(0)
dpx = [0]*(len(x)+1)
dpy = [0]*(len(y)+1)
dpx[0] = set([0])
dpy[0] = set([0])
for i in range(1,len(x)+1):
  s1 = set([v + x[i-1] for v in dpx[i-1]])
  s2 = set([v - x[i-1] for v in dpx[i-1]])
  if i == 1:
    dpx[i] = s1
  else:
    dpx[i] = s1|s2
for i in range(1,len(y)+1):
  s1 = set([v + y[i-1] for v in dpy[i-1]])
  s2 = set([v - y[i-1] for v in dpy[i-1]])
  dpy[i] = s1|s2
if gx in dpx[-1] and gy in dpy[-1]:
  print("Yes")
else:
  print("No")
