a,b=map(int,input().split())
p=1
ans=0
while p<b:
    p=p-1
    p=p+a
    ans+=1
print(ans)