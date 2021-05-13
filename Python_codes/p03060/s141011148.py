n=int(input())
v=list(map(int,input().split()))
c=list(map(int,input().split()))
value=[]
for i in range(n):
    value.append(v[i]-c[i])
ans=0
for i in range(len(value)):
    if value[i]>0:
        ans+=value[i]
print(ans)