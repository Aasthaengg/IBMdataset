from bisect import bisect_left

n, k = map(int, input().split())
x = list(map(int, input().split()))
ans = 0
min_dis = 10 ** 20
a = 0
for i in range(n - k + 1):
    dis = x[i + k - 1] - x[i] + min(abs(x[i]), abs(x[i + k - 1]))
    if min_dis > dis:
        ans = dis
        min_dis = dis
print(ans)
