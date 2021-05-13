n=int(input())
a=list(map(int,input().split()))
b=[0]*n
ans=0
for i in a:
    if i>n:
        ans+=1
    else:
        b[i-1]+=1
for i in range(n):
    if b[i]>i:
        ans+=b[i]-i-1
    else:
        ans+=b[i]
print(ans)