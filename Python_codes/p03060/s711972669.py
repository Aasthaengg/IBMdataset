n=int(input())
v=list(map(int,input().split()))
c=list(map(int,input().split()))
ans=[]
for i in range(n):
    if v[i]-c[i]>0:
        k=v[i]-c[i]
        ans.append(k)
print(sum(ans))