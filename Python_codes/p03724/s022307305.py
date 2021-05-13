# 2019/10/05

n,m=map(int,input().split())
res=[0]*n

for _ in range(m):
    a,b=(map(int,input().split()))
    res[a-1]+=1
    res[b-1]+=1

for e in res:
    if e%2:
        print('NO')
        exit()
else:
    print('YES')