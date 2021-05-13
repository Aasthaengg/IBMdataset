import bisect
a,b,q=map(int,input().split())
s=[int(input()) for i in range(a)]
t=[int(input()) for i in range(b)]
s.sort()
t.sort()
for _ in range(q):
  x=int(input())
  idx1=bisect.bisect_left(s,x)
  idx2=bisect.bisect_left(t,x)
  d=[]
  if idx1<a and idx2<b:
    d.append(max(s[idx1]-x,t[idx2]-x))
  if 1<=idx1 and 1<=idx2:
    d.append(max(x-s[idx1-1],x-t[idx2-1]))
  if 1<=idx1 and idx2<b:
    d.append((t[idx2]-x)*2+x-s[idx1-1])
    d.append((x-s[idx1-1])*2+t[idx2]-x)
  if idx1<a and 1<=idx2:
    d.append((s[idx1]-x)*2+x-t[idx2-1])
    d.append((x-t[idx2-1])*2+s[idx1]-x)
  print(min(d))