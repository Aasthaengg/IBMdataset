n=int(input())
a=sorted(list(map(int,input().split())),reverse=True)
s=sum(a)-a[0]
ans=1
for i in range(1,n):
    if s*2>=a[i-1]:
        ans+=1
        s-=a[i]
    else:
        break
print(ans)
