h,w=map(int,input().split())
a=[input() for _ in range(h)]

ans = [ [ 12345678 for _ in range(w) ] for d in range(h)]

for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            ans[i][j] = 0

for i in range(h):
    for j in range(1,w):
        ans[i][j] = min(ans[i][j], ans[i][j-1]+1)
    for j in range(w-1-1,-1,-1):
        ans[i][j] = min(ans[i][j],ans[i][j+1]+1)

for j in range(w):
    for i in range(1,h):
        ans[i][j] = min(ans[i][j], ans[i-1][j]+1)
    for i in range(h-1-1,-1,-1):
        ans[i][j] = min(ans[i][j], ans[i+1][j]+1)

ma =-4
for x in ans:
    for y in x:
        ma = max(ma,y)
print(ma)