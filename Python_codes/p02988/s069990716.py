n=int(input())
l=list(map(int,input().split()))
ans=0
for i in range(n-2):
    a=l[i:i+3]
    b=a[1]
    c=sorted(a)
    if b==c[1]:
        ans+=1
print(ans)