n=int(input())
a=list(str(input()))
b=list(str(input()))
c=list(str(input()))

ans=0
for i in range(n):
    l=set(list(a[i]+b[i]+c[i]))
    if len(l)==3:ans+=2
    elif len(l)==2:ans+=1
print(ans)