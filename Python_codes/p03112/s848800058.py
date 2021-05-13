import numpy as np
A, B, Q, *L = map(int, open(0).read().split())
s = L[:A]
t = L[A:A+B]
x = L[A+B:]

s = [-float('inf')]+s+[float('inf')]
t = [-float('inf')]+t+[float('inf')]
sls = np.searchsorted(s,x)
tls = np.searchsorted(t,x)
for ar, br, c in zip(sls,tls,x):
  bl = br-1
  al = ar-1
  n = s[ar]-t[bl]+min(s[ar]-c,c-t[bl])
  m = t[br]-s[al]+min(t[br]-c,c-s[al])
  p = c-min(t[bl],s[al])
  q = max(s[ar],t[br])-c
  print(min(n,m,p,q))