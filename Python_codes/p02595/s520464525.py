N,D=list(map(int,input().split()))
ans=0
for i in range(N):
   a,b=list(map(int,input().split()))
   if D**2>=a**2+b**2:
      ans+=1
print(ans)