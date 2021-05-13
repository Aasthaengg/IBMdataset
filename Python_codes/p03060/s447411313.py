n=int(input())
v=list(map(int,input().split()))
c=list(map(int,input().split()))
ans=[]
for i in range(2**n):
    x=0
    y=0
    for j in range(n):
        if (i>>j)&1:
            x+=v[j]
            y+=c[j]
    ans.append(x-y)
print(max(ans))
