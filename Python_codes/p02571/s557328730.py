s=input()
t=input()
q=10**18
for i in range(len(s)-len(t)+1):
    ans=0
    for j in range(len(t)):
        if t[j]!=s[i+j]:
            ans+=1
    q=min(ans,q)
print(q)