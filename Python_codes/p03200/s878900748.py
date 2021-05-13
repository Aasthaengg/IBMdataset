s=input()

ans=0
cnt=0
for i,j in enumerate(s):
  if j=="W":
    ans+=i-cnt
    cnt+=1
    
print(ans)