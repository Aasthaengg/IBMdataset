import bisect
a,b,q=map(int,input().split())
s=[int(input()) for i in range(a)]
t=[int(input()) for i in range(b)]
for i in range(q):
  x=int(input())
  idxS=bisect.bisect_left(s,x)
  idxT=bisect.bisect_left(t,x)
  d=[]
  if idxS<a and idxT<b:
    d.append(max(s[idxS]-x,t[idxT]-x))
  if 1<=idxS and 1<=idxT:
    d.append(max(x-s[idxS-1],x-t[idxT-1]))
  if 1<=idxS and idxT<b:
    d.append((t[idxT]-x)*2+x-s[idxS-1])
  if 1<=idxT and idxS<a:
    d.append((s[idxS]-x)*2+x-t[idxT-1])
  if idxT<b and 1<=idxS:
    d.append((x-s[idxS-1])*2+t[idxT]-x)
  if idxS<a and 1<=idxT:
    d.append((x-t[idxT-1])*2+s[idxS]-x)
  print(min(d))