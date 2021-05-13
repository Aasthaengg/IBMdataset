n=int(input())
a=list(map(int,input().split()))
a=sorted(a,reverse=True)
ans=0
for i in range(n*2):
    if i%2 == 1:
        ans+=a[i]
print(ans)