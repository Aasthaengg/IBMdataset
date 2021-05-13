n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))+[0]
ans=0
bn,ba=0,0
for i in a:
    ans+=b[i-1]
    if bn+1==i:
        ans+=ba
    bn=i
    ba=c[i-1]
print(ans)