N,T = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
cur = 0
for i in range(1,N):
    b = A[i]
    a = A[i-1]
    if b-a<T:
        cur += b-a
    else:
        cnt += cur+T
        cur = 0
cnt += cur+T
print(cnt)