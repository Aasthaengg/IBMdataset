N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt = 0
for i in range(N):
    b = B[i]
    if A[i]>=b:
        cnt += b
        b = 0
    else:
        cnt += A[i]
        b -= A[i]
    if A[i+1]>=b:
        cnt += b
        A[i+1] -= b
    else:
        cnt += A[i+1]
        A[i+1]=0
print(cnt)