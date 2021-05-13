N,T=map(int, input().split())
A=list(map(int, input().split()))
if N==1:
  print(1)
  exit()
mn=10**9+1
V=-1*10**9
cnt=0
for i in range(N):
  if V==A[i]-mn:
    cnt+=1
  elif V<A[i]-mn:
    V=A[i]-mn
    cnt=1
  mn=min(A[i],mn)
print(cnt)