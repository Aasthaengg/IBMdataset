N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
for i in range(N-1):
    for j in range(i+1,N):
        amin = 10**10
        for k in range(N):
            if k!=i and k!=j:
                amin = min(amin,A[i][k]+A[k][j])
        if A[i][j]>amin:
            cnt = -1
            break
        elif A[i][j]<amin:
            cnt += A[i][j]
    if cnt==-1:break
print(cnt)