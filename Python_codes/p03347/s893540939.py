N = int(input())
cnt = 0
A = [int(input()) for _ in range(N)]
if A[0]!=0:
    cnt = -1
else:
    for i in range(1,N):
        if A[i]==A[i-1]+1:
            continue
        elif A[i]<=A[i-1]:
            cnt += A[i-1]
        else:
            cnt = -1
            break
    if cnt>=0:
        cnt += A[N-1]
print(cnt)  