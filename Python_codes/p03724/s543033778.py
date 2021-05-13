# B - Unplanned Queries
n,m=map(int,input().split())
cnt=[0]*n
G=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    cnt[a-1]+=1
    cnt[b-1]+=1
for c in cnt:
    if c%2!=0:
        print('NO')
        exit()
print('YES')
