N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
cnt = 0
for i in range(N)[::-1]:
    if (A[i][0] + cnt)%A[i][1] != 0:
        cnt += A[i][1] - (A[i][0] + cnt)%A[i][1]
print(cnt)