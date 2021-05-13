s=input()
n=len(s)
ans=0
for i,j in zip(s[:n//2],s[:n//2-1:-1]):
  if i!=j:
    ans+=1
print(ans)