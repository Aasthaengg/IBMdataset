m,k=map(int,input().split())
if 1<<m<=k:exit(print(-1))
if m==1:exit(print(*[-1]if k else [0,0,1,1]))
l=[i for i in range(1<<m)if i!=k]
print(*(l+[k]+l[::-1]+[k]))