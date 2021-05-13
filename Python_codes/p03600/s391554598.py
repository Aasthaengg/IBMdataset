

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            # 
            if A[i][j] > A[i][k] + A[k][j]:
                print(-1)
                exit()


ans = 0
for i in range(N):
    for j in range(i+1,N):

        f = True
        for k in range(N):
            if k == i or k == j:
                continue
            if A[i][j] == A[i][k] + A[k][j]:
                f = False
                break
        
        if f:
            #辺i->jを足す
            ans += A[i][j]


print(ans)