N,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
A = sorted(A,key=lambda x:x[0])
cnt = 0
i = 0
while K>cnt:
    cnt += A[i][1]
    i += 1
print(A[i-1][0])