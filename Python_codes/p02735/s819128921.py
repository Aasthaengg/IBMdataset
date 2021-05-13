h,w=map(int,input().split())

m=[input() for i in range(h)]


cnt=[[1000000 for i in range(w)] for j in range(h)]

if m[0][0]=="#":
    cnt[0][0]=1
else:
    cnt[0][0]=0

for y in range(h):
    for x in range(w):
        if x>0:
            if m[y][x-1]=="." and m[y][x]=="#":
                cnt[y][x]=min(cnt[y][x],cnt[y][x-1]+1)
            else:
                cnt[y][x]=min(cnt[y][x],cnt[y][x-1])
        if y>0:
            if m[y-1][x]=="." and m[y][x]=="#":
                cnt[y][x]=min(cnt[y][x],cnt[y-1][x]+1)
            else:
                cnt[y][x]=min(cnt[y][x],cnt[y-1][x])


print(cnt[h-1][w-1])