n=int(input())
a=list(input())
b=list(input())
c=list(input())
ans=0
for i in range(n):
    if a[i]!=b[i] and a[i]!=c[i] and b[i]!=c[i]:
        ans+=2
    elif a[i]==b[i] and b[i]!=c[i]:
        ans+=1
    elif a[i]==c[i] and b[i]!=c[i]:
        ans+=1
    elif c[i]==b[i] and a[i]!=c[i]:
        ans+=1
    else:
        ans+=0
print(ans)