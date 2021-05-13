s=input()
n=len(s)
g=0
p=0
ans=0
for i in range(n):
    if s[i]=="g":
        if p+1<=g:
            ans+=1
            p+=1
        else:
            g+=1
    else:
        if p+1<=g:
            p+=1
        else:
            g+=1
            ans-=1
print(ans)
