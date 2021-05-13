n=int(input())
a=input()
b=input()
c=input()
ans=0
for i in range(n):
    d=set([a[i],b[i],c[i]])
    x=len(d)
    if x==3:
        ans+=2
    elif x==2:
        ans+=1
print(ans)
