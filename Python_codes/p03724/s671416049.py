n,m = map(int, input().split())
ab=[list(map(int,input().split())) for i in range(m)]
cnt=[0]*n

for tmp in ab:
    a,b=tmp
    cnt[a-1]+=1
    cnt[b-1]+=1

for c in cnt:
    if c%2!=0:
        print("NO")
        exit()
print("YES")