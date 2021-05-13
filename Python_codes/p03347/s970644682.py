N = int(input())
A = [int(input()) for _ in range(N)]
cnt = 0
if(A[0] != 0):
    cnt = -1
else:
    cur = A[0]
    for i in range(1,N):
        if(A[i] - A[i-1] > 1):
            cnt = -1
            break
        elif(A[i] - A[i-1] == 1):
            cnt += 1
            cur = A[i]
        else:
            cnt += A[i]
            cur = A[i]
print(cnt)