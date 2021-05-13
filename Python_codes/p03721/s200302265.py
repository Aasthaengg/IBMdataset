N,K = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(N)]
a.sort()
cnt = 0
for i in range(N):
    cnt += a[i][1]
    if cnt >= K:
        print(a[i][0])
        exit()