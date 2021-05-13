s=sorted(map(int,input().split()))
ans=0
while s[0]+2<=s[2]:
    s[0]+=2
    ans+=1
while s[1]+2<=s[2]:
    s[1]+=2
    ans+=1
    
s=sorted(s)
if s[0]==s[2]:
    print(ans)
elif s[0]==s[1]:
    print(ans+1)
else:
    print(ans+2)