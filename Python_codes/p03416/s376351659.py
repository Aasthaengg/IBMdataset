a,b=map(int,input().split())
ans=0
for i in range(a,b+1):
    s=str(i)
    if s[:2]==s[3:][::-1]:ans+=1 
print(ans)