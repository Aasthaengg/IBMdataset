ab=[list(map(int,input().split())) for i in range(3)]
cnt=[0,0,0,0]
ans='YES'
for i in ab:
    for j in i:
        cnt[j-1]+=1
for i in cnt:
    if i>=3:
        ans='NO'
print(ans)