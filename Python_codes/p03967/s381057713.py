s=input()
N=len(s)

ans=0
g=0
p=0
for i in range(N):
    if s[i]=="p":
        p+=1
        if p>g:
            ans-=1
            p-=1
            g+=1 
    else:
        g+=1
        val=g-p
        if val==2:
            ans+=1
            g-=1
            p+=1
print(ans)