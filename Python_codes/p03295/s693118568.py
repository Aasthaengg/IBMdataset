n,m=map(int,input().split())
ab=[list(map(int, input().split())) for _ in range(m)]
# bに注目してソート
ab = sorted(ab, key=lambda x: x[1])
ans=0
left=-1
for i in range(m):
    if ab[i][0]<=left<ab[i][1]:
        continue
    left=ab[i][1]-0.5
    ans+=1
print(ans)
