n,T=map(int,input().split())
c=[]
t=[]
for i in range(n):
  cd,td=map(int,input().split())
  c.append(cd)
  t.append(td)

mxc=max(c)
for i in range(n):
  if t[i]>T:
    c[i]=mxc+1

if min(c)>mxc:
  print("TLE")
else:
  print(min(c))