N,x = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
for i in range(1,N):
    if A[i]+A[i-1]>x:
        d = A[i]+A[i-1]-x
        if A[i]>=d:
            A[i] -= d
            cnt += d
        else:
            A[i]=0
            cnt += A[i]
            d -= A[i]
            A[i-1] -= d
            cnt += d
print(cnt)