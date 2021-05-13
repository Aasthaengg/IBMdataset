N=int(input())
S=input()
ap=[0]*(N+1)
bp=[0]*(N+1)
a=0
b=0
for i in range(N):
  if S[i]=='W':
    a+=1
  else:
    b+=1
  ap[i+1]=a
  bp[i+1]=b
ans=10**9
for j in range(1,N+1):
  ans=min(ap[j-1]+bp[N]-bp[j],ans)
print(ans)