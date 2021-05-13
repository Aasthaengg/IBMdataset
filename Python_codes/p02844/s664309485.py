n=int(input())
s=list(input())
d={}
ans=0
for x in range(n-2):
  if s[x] not in d:
    d[s[x]]=0
    for y in range(x+1,n-1):
      if (s[x]+s[y]) not in d:
        d[(s[x]+s[y])]=0
        for z in range(y+1,n):
          if (s[x]+s[y]+s[z]) not in d:
            d[(s[x]+s[y]+s[z])]=0
            ans+=1
    
print(ans)   