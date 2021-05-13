n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
ans=0
con=10000000
for i in a:
    ans+=b[i-1]
    if con+1==i :
        ans+=c[con-1]
    con=i
print(ans)