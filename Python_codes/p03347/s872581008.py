N = int(input())
A = [int(input()) for _ in range(N)]

if A[0] > 0:
    print(-1)
    exit()

tmp = 0
for i in range(1,N):
    if A[i] <= i and A[i] <= tmp+1:
        tmp = A[i]
    else:
        print(-1)
        exit()

tmp = 0
ans = 0
for i in range(1,N):
    if A[i] < tmp+1:
        ans += tmp
    tmp = A[i]

ans += tmp

print(ans)