s=input()
t=input()

ans=0
i=0
while i<len(s):

    if s[i]==t[i]:
        ans+=1

    i+=1
    
print(ans)