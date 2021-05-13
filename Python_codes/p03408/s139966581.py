n=int(input())
d={}
for i in range(n):
    x=input()
    if(x not in d):
        d[x]=1
    else:
        d[x]+=1
m=int(input())
for i in range(m):
    x=input()
    if(x not in d):
        d[x]=-1
    else:
        d[x]-=1
l=list(d.values())
print(max(max(l),0))
