n=int(input())
a=list(input())
b=list(input())
c=list(input())

ans=0

for i in range(n):
    if a[i]==b[i] and b[i]==c[i]:
        continue
    elif a[i]!=b[i] and b[i]==c[i]:
        ans+=1
    elif a[i]!=c[i] and a[i]==b[i]:
        ans+=1
    elif b[i]!=c[i] and a[i]==c[i]:
        ans+=1
    else:
        ans+=2
print(ans)