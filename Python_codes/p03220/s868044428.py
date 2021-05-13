n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

diff_min = float('inf')
for i in range(n):
    diff = abs(a - (t - h[i] * 0.006))
    if diff < diff_min:
        ans = i + 1
        diff_min = diff
print(ans)
