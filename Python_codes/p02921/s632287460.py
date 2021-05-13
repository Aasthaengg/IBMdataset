s=input() ; t=input() ; ans=0
for i in [1,2,3]:
    i-=1
    if s[i]==t[i]:
        ans+=1
print(ans)