n,x=map(int,input().split())
l=list(map(int,input().split()))
d=[0]

for i in range(1,n+1):
    temp=d[i-1]+l[i-1]
    if temp>x:
        ans=i
        break
    d.append(temp)

else:
    ans=n+1

print(ans)