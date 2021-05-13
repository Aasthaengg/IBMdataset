n=int(input())
b=list(map(int,input().split()))
ans=b[0]+b[-1]

for i in range(n-2):
  if b[i]<=b[i+1]:
    ans+=b[i]
    
  else:
    ans+=b[i+1]
  
print(ans)