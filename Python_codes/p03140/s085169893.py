n= int(input())
a=input()
b=input()
c=input()
d=[{a[i],b[i],c[i]} for i in range(n)]
ans=0
for i in range(n):
    ans+=len(d[i])-1
print(ans)