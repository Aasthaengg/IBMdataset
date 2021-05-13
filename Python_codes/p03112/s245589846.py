A,B,Q=map(int,input().split())
S=[int(input()) for i in range(A)]+[0,10**10+1]
T=[int(input()) for i in range(B)]+[0,10**10+1]
S=sorted(S)
T=sorted(T)
import bisect
for i in range(Q):
  x=int(input())
  si=bisect.bisect_left(S,x)
  if si==1:
    s1,s2=S[si],S[si]
  elif si==A+1:
    s1,s2=S[si-1],S[si-1]
  else:
    s1,s2=S[si-1],S[si]
  ti=bisect.bisect_left(T,x)
  if ti==1:
    t1,t2=T[ti],T[ti]
  elif ti==B+1:
    t1,t2=T[ti-1],T[ti-1]
  else:
    t1,t2=T[ti-1],T[ti]
  ans=min(abs(x-s1)+min(abs(s1-t1),abs(s1-t2)),
         abs(s2-x)+min(abs(s2-t1),abs(s2-t2)),
         abs(x-t1)+min(abs(t1-s1),abs(t1-s2)),
         abs(t2-x)+min(abs(t2-s1),abs(t2-s2)))
  print(ans)