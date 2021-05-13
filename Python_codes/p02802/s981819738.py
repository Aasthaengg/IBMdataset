n,m=map(int,input().split())
l=[0]*n
d=[0]*n
for i in range(m):
    s=input().split()
    x=int(s[0])
    if(s[1]=='AC'):
        l[x-1]=1
    else:
        if(l[x-1]==1):
            continue
        else:
            d[x-1]+=1
p=0
for i in range(n):
    if(l[i]==1):
        p+=d[i]
print(sum(l),p)
