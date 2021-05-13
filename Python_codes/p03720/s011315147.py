n,m=map(int,input().split())
abl=[list(map(int,input().split())) for _ in range(m)]

ans=[0]*n
for ab in abl:
    ans[ab[0]-1]+=1
    ans[ab[1]-1]+=1

for i in ans:
    print(i)
