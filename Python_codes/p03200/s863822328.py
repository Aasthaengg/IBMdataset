s=list(input())
co=0
ans=0
for (c,i) in zip(s,range(len(s))):

  if c== "W":
    ans+=i-co
    co+=1
    
print(ans)