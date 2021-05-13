N,M = map(int,input().split())
place = [list(map(int,input().split())) for _ in range(N)]
check = [list(map(int,input().split())) for _ in range(M)]
for x,y in place:
    tmp = 10**9
    for i in range(M):
        dis = abs(x-check[i][0]) + abs(y-check[i][1])
        if tmp > dis:
            tmp = dis
            ans = i+1
    print(ans)