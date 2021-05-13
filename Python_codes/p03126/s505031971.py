N, M = map(int, input().split())
KA = [list(map(int,input().split())) for _ in range(N)]

lst = [0]*M

for i in range(N):
    for j in range(KA[i][0]):
        lst[KA[i][j+1]-1] += 1

ans = lst.count(N)
print(ans)
