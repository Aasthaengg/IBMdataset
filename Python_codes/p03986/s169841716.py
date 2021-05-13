x=input()
ans=len(x)
p=0
for i in x:
    if i=="S":
        p+=1
    if p>0 and i=="T":
        p-=1
        ans-=2
print(ans)