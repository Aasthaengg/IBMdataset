s=input()
p,g=0,0
ans=0
for i in s:
    if i=="g":
        if p+1<=g:
            ans+=1
            p+=1
        else:
            g+=1
    if i=="p":
        if p+1<=g:
            p+=1
        else:    
            ans-=1
            g+=1
print(ans)   