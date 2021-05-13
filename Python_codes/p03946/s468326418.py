N,T=map(int,input().split())
A=list(map(int,input().split()))

r=N-1
p=-1
for l in reversed(range(N)):
  if A[l]>A[r]:
    r=l
  else:
    if A[r]-A[l]==p:
      ans+=1
    elif A[r]-A[l]>p:
      ans=1
      p=A[r]-A[l]
      
print(ans)