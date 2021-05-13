N,T = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
cur = 0
for i in range(1,N):
    if A[i]-A[i-1]>T:
        cnt += A[i-1]-cur+T
        cur = A[i]
cnt += A[N-1]+T-cur
print(cnt)