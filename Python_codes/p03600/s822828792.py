N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        cnt += A[i][j]
flg = 0
B = [[0 for _ in range(N)] for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][j]>A[i][k]+A[k][j]:
                flg = -1
                break
            elif A[i][j]==A[i][k]+A[k][j] and A[i][k]*A[k][j]>0 and B[i][j]==0:
                cnt -= A[i][j]
                B[i][j]=1
        if flg==-1:break
    if flg==-1:break
if flg==-1:
    print(-1)
else:
    print(cnt//2)          