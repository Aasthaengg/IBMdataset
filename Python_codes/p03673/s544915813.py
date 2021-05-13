N = int(input())
A = list(map(int,input().split()))
ans = [0 for _ in range(N)]
l = 0
r = N - 1
flg = 1
for i in range(N - 1, -1, -1):
    if flg:
        flg = 0
        ans[l] = A[i]
        l += 1
    else:
        flg = 1
        ans[r] = A[i]
        r -= 1
print(*ans)