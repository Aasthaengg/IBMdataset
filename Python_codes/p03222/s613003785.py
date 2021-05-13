h,w,k = map(int,input().split())
if w == 1:
  print(1)
  exit()
a = [0]*(w+2)
a[1] = 1
f = [0]*(w-1)
p = 0
q = 1
for i in range(w-1):
  f[i] = p+q
  q = p + q
  p = q - p  
f.append(1)
b = []
mod = 10**9+7
for i in range(w):
  if i == 0:
    b.append([0,f[w-2],f[w-3]])
  elif i == w-1:
    b.append([f[w-3],f[w-2],0])
  else:
    b.append([f[i-2]*f[w-i-2],f[i-1]*f[w-i-2],f[i-1]*f[w-i-3]])
for _ in range(h):
  newa = [0]*(w+2)
  for i in range(1,w+1):
    newa[i] = (a[i-1]*b[i-1][0]+a[i]*b[i-1][1]+a[i+1]*b[i-1][2])%mod
  a = newa
print(a[k])