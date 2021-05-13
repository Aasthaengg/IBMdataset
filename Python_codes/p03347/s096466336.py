N = int(input())
A = [int(input()) for _ in range(N)]
cnt = A[-1]
flag = 0
for i in range(N-2,-1,-1):
    if A[i]==A[i+1] or A[i]>A[i+1]:
        cnt += A[i]
    elif A[i] == A[i+1]-1:
        continue
    else:
        flag = 1
        break
if A[0]!=0:
    flag = 1
if flag==0:
    print(cnt)
else:
    print(-1)