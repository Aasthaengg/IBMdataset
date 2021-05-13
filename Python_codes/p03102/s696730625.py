N, M, C = map(int,input().split())

bl = list(map(int,input().split()))
al = []
for i in range(N):
    al.append(list(map(int,input().split())))

cnt = 0
for i in range(N):
    wa = 0
    for j in range(M):
        wa += al[i][j]*bl[j]
    if wa + C > 0:
        cnt += 1

print(cnt)