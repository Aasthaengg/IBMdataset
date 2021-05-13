n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
d_min = 99999
ans = 0
for i in range(n):
    d = abs(t - a - h[i] * 0.006)
    if d < d_min:
        d_min = d
        ans = i + 1
print(ans)
