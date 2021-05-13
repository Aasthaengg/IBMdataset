def warshall_floyd(d):
    for i in range(10):
        for j, c2 in enumerate(d[j][i] for j in range(10)):
            for k, (c1,c3) in enumerate(zip(d[j], d[i])):
                if c1 > c2+c3:
                    d[j][k] = c2+c3
    return d

h,w = map(int,input().split())
d=[list(map(int,input().split())) for _ in range(10)] 
a=[list(map(int,input().split())) for _ in range(h)]
a_cnt=[0]*10
for i in range(h):
    for j in range(w):
        if a[i][j]==-1:
            continue
        a_cnt[a[i][j]]+=1
d=warshall_floyd(d)
ans=0
for i,j in enumerate(a_cnt):
    ans+=d[i][1]*j
print(ans)