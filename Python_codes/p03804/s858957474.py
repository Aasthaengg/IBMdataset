n,m=map(int,input().split())
a=[]
b=[]
for _ in range(n):
    x=[1 if s=='#' else 0 for s in input()]
    a.append(x)

for _ in range(m):
    x=[1 if s=='#' else 0 for s in input()]
    b.append(x)

for h in range(n-m+1):
    for w in range(n-m+1):
        tmpa=[a[x][w:w+m] for x in range(h,h+m)]
        if tmpa==b:
            print('Yes')
            exit()
print('No')