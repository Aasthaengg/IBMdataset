n,m=map(int,input().split())
cnt=[0]*n
for _ in range(m):
    a,b=map(int,input().split())
    cnt[a-1]+=1
    cnt[b-1]+=1
print(*cnt)
