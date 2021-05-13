s=input()
now,ans=0,0
while now<len(s)-1:
    if s[now]!=s[now+1]:
        ans+=1
    now+=1
print(ans)