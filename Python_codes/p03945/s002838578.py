s=list(input())
a=s[0]
ans=0
for i in s:
    if i !=a:
        ans+=1
        a=i

print(ans)