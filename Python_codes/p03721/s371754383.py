N, K = list(map(int,input().split()))
A = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
A = sorted(A, key = lambda x: x[0])
for i in range(N):
    cnt += A[i][1]
    if cnt >= K:  
        print(A[i][0])
        break