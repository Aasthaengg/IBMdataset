n=int(input())
a=input()
b=input()
c=input()

ans=0

for i in range(n):
    if a[i]==b[i]:
        if b[i]!=c[i]:
            ans+=1
    else:
        if b[i]==c[i]:
            ans+=1
        elif a[i]==c[i]:
            ans+=1
        else:
            ans+=2

print(ans)