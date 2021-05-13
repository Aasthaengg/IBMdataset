x=input()
l=len(x)
c=0
ans=0
for i in range(l):
    if x[i]=='S':
        c+=1
    else:
        if c>0:
            ans+=1
        c-=1
    if c<0:
        c+=1
print(l-ans*2)