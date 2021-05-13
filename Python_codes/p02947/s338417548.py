n=int(input())
s=[]
for i in range(n):
    x=list(input())
    x=sorted(x)
    s.append("".join(x))
s=sorted(s)
m=1
ans=0
for i in range(n-1):
    if s[i]==s[i+1]:
        m+=1
    else:
        ans+=m*(m-1)//2
        m=1
ans+=m*(m-1)//2
print(ans)
    
