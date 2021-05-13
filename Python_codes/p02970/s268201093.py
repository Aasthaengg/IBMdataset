n,d=map(int,input().split())

ans=1
n-=1
for i in range(1,20):
    n -= 2*d
    if n<=0 :
        break
    n-=1
    ans+=1
print(ans)