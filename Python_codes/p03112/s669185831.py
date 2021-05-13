import bisect
A,B,Q=map(int,input().split())
INF=10**12
S=[-INF]
for i in range(A):
  S.append(int(input()))
S.append(INF)
T=[-INF]
for i in range(B):
  T.append(int(input()))
T.append(INF)
for i in range(Q):
  x=int(input())
  sh=S[bisect.bisect_left(S,x)]
  sl=S[bisect.bisect_left(S,x)-1]
  th=T[bisect.bisect_left(T,x)]
  tl=T[bisect.bisect_left(T,x)-1]
  a1=abs(x-sh)+abs(sh-th)
  a2=abs(x-sl)+abs(sl-th)
  a3=abs(x-sh)+abs(sh-tl)
  a4=abs(x-sl)+abs(sl-tl)
  a5=abs(x-th)+abs(th-sh)
  a6=abs(x-tl)+abs(tl-sh)
  a7=abs(x-th)+abs(th-sl)
  a8=abs(x-tl)+abs(tl-sl)
  print(min(a1,a2,a3,a4,a5,a6,a7,a8))