N = int(input())
A = [int(input()) for _ in range(N)]

if A[0] != 0:
    print(-1)
    exit()

ans = 0
for i in range(1, N):
    if A[i]-A[i-1] >= 2:
        print(-1)
        exit()
    elif A[i]-A[i-1] == 1:
        ans += 1
    else:
        ans += A[i]
print(ans)
