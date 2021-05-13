N = int(input())
A = [int(input()) for _ in range(N)]
flag = 0
cnt = A[N-1]
for i in range(N-2,-1,-1):
    if A[i]==A[i+1]-1:continue
    elif A[i]>=A[i+1]:
        if A[i]>0:
            cnt += A[i]
    else:
        flag = 1
        break
if A[0]>0 or flag==1:
    print(-1)
else:
    print(cnt)