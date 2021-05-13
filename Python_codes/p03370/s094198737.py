n,x=map(int,input().split())
list_m=[int(input()) for i in range(n)]
for i in range(n):
    x-=list_m[i]
ans=n
ans+=x//(min(list_m))
print(ans)