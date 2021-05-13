N=int(input())
A=list(map(int,input().split()))
ans=1
vec=0
for i in range(N-1):
  now=A[i+1]-A[i]
  if vec*now<0:
    ans+=1
    vec=0
  elif vec==0:
    vec=now
print(ans)
