N = int(input())
K = int(input())
x = list(map(int, input().split()))

ans = 0

for i in range(N):
    dist_zero = x[i] - 0
    dist_K = abs(x[i] - K)
    if dist_zero <= dist_K:
        ans += dist_zero * 2
    else:
        ans += dist_K * 2

print(ans)
