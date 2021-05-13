n=int(input())
a=[int(i)for i in input().split()]

ans=0
for i in a:
    tmp=i
    while tmp%2==0:
        ans+=1
        tmp=tmp//2
print(ans)