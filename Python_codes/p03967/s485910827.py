s=input()
n=len(s)

ans=0

g=0 ; p=0
for  i in range(n):
    if g==p:
        g+=1
        if s[i]=="p": ans-=1
    else:
        if s[i]=="p":
            p+=1 
        else:
            p+=1
            ans+=1
print(ans)
