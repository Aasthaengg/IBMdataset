import sys
inf = float('inf')
N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    d[i][i] = 0
ans=0
for a in range(N):
    for b in range(N):
        flag = True
        for i in range(N):
            if i == a or i == b:
                continue
            if d[a][i]+d[i][b]<d[a][b]:
                print(-1)
                sys.exit()
            if d[a][i]+d[i][b]==d[a][b]:
                flag = False
                break
        if flag:
            ans+=d[a][b]
            
print(ans//2)
    




