from bisect import *
A,B,Q=map(int,input().split())
INF=10**15
S=[-INF*10,-INF]
for i in range(A):
  S.append(int(input()))
S.append(INF)
S.append(INF*10)
T=[-INF*10,-INF]
for i in range(B):
  T.append(int(input()))
T.append(INF)
T.append(INF*10)
D,E,F,G,V,W,X,Y,Z,P=0,0,0,0,0,0,0,0,0,0
for i in range(Q):
  X=int(input())
  V=bisect_left(S,X)
  Y,Z=S[V-1],S[V]
  D,E=abs(X-Y),abs(X-Z)
  V,W=bisect_left(T,Y),bisect_left(T,Z)
  F,G=min(abs(Y-T[V-1]),abs(Y-T[V])),min(abs(Z-T[W-1]),abs(Z-T[W]))
  P=min(D+F,E+G)
  V=bisect_left(T,X)
  Y,Z=T[V-1],T[V]
  D,E=abs(X-Y),abs(X-Z)
  V,W=bisect_left(S,Y),bisect_left(S,Z)
  F,G=min(abs(Y-S[V-1]),abs(Y-S[V])),min(abs(Z-S[W-1]),abs(Z-S[W]))
  print(min(P,D+F,E+G))