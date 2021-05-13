n=int(input())
a=input()
b=input()
c=input()
ans=0
for i in range(n):
    if a[i]!=b[i] and a[i]!=c[i] and b[i]!=c[i]:
        ans+=2
    elif (a[i]==b[i] and a[i]!=c[i]) or (a[i]==c[i] and a[i]!=b[i]) or (b[i]==c[i] and a[i]!=b[i]):
        ans+=1
print(ans)