N = int(input())
A = [int(input()) for _ in range(N)]

flag = (A[0] == 0)
ans = 0

for i in range(1, N):
    d = A[i] - A[i - 1]
    if d > 1:
        flag = False
    elif d == 1:
        ans += 1
    else:
        ans += A[i]

if flag is False:
    ans = -1

print(ans)