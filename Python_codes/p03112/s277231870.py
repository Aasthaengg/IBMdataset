a,b,q=map(int,input().split())
s=[int(input()) for _ in range(a)]
t=[int(input()) for _ in range(b)]
x=[int(input()) for _ in range(q)]
from bisect import bisect_left
for xi in x:
  ans=float('inf')
  si=bisect_left(s,xi)
  ti=bisect_left(t,xi)
  # 東に進むだけ
  if xi<=s[-1] and xi<=t[-1]:
    ans=min(ans,max(s[si]-xi,t[ti]-xi))
  # 西に進むだけ
  if xi>=s[0] and xi>=t[0]:
    ss=0 if si<a and xi-s[si]==0 else xi-s[si-1]
    tt=0 if ti<b and xi-t[ti]==0 else xi-t[ti-1]
    ans=min(ans,max(ss,tt))
    
  # 東に進んだあと西 or 西に進んだあと東
  # 西の神社、東の寺
  if s[0]<=xi and xi<=t[-1]:
    w=xi-s[si-1]
    e=t[ti]-xi
    tmp=2*min(w,e)+max(w,e)
    ans=min(ans,tmp)
  # 西の寺、東の神社
  if t[0]<=xi and xi<=s[-1]:
    w=xi-t[ti-1]
    e=s[si]-xi
    tmp=2*min(w,e)+max(w,e)
    ans=min(ans,tmp)
  print(ans)
