n,m,c = map(int,input().split())

bl = list(map(int,input().split()))
al = [list(map(int,input().split())) for i in range(n)]
cnt = 0

for i in range(n):
    total = 0
    for j in range(m):
        total+=bl[j]*al[i][j]
    total+=c
    if 0 < total:
        cnt+=1
print(cnt)

