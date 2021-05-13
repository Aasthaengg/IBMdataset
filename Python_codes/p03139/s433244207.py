N,A,B=map(int,input().split())

S=min(A,B)
T=0
if A+B >N:
  T=(A+B)-N

print(S,T)