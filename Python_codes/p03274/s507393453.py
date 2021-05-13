from bisect import bisect_right, bisect_left

N, K = map(int, input().split())
x = list(map(int, input().split()))

ans = 4*10**8 + 1
x_0 = bisect_right(x, 0)
x_1 = bisect_left(x, 0) - 1

for i in range(N-K+1):
    if i + K -1 >= x_1 and i <= x_0:
        if x[i + K - 1] <= 0:
            ans = min(ans, -x[i])
        elif x[i] >= 0:
            ans = min(ans, x[i + K - 1])
        else:
            ans = min(ans, min(-x[i]*2 + x[i+K-1], -x[i] + x[i+K-1]*2))
print(ans)