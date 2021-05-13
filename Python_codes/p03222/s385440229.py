h,w,k=map(int,input().split())
mod = 10**9+7
l=[]
a=[[0 for i in range(w)] for j in range(w)]

def dsf(i,v):
  if i==w-1:
    t = list()
    for j in range(0,w):
      t.append(j)
    for j in range(w-1):
      if v & 2**(j):
        t[j],t[j+1]=t[j+1],t[j]
    for x in range(w):
      a[x][t[x]] += 1
    l.append(v)
  else:
    dsf(i+1,v)
    if v & 2**(i-1) == 0:
      dsf(i+1,v | 2**i)

if w==1:
  print(1)
  exit()

dsf(1,0)
dsf(1,1)

t=[[0 for i in range(w)] for j in range(2)]
t[0][0]=1

for i in range(h):
  for j in range(w):
    t[(i+1)%2][j] = 0
    t[i%2][j] %= mod
  for j in range(w):
    for x in range(w):
     t[(i+1)%2][x] += t[i%2][ｊ] * a[j][x]

print(t[h%2][k-1]%mod)
