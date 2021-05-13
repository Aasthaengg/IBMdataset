s=list(input())
ans=999
for i in range(len(s)-2):
    p="".join(s[i:i+3])
    p=int(p)
    p=abs(753-p)
    ans=min(p,ans)
    
print(ans)