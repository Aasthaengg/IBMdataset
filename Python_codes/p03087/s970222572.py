N,Q=map(int,input().split())
S=input()
A=[]
C=[]
for i in range(N-1):
  if S[i]=='A' and S[i+1]=='C':
    A.append(i+1)
    C.append(i+2)
import bisect
for i in range(Q):
  l,r=map(int,input().split())
  a=bisect.bisect_left(A,l)
  c=bisect.bisect_right(C,r)
  print(c-a)