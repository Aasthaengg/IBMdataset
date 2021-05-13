n = int(input())
t, a = map(int, input().split())
(*h,) = map(int, input().split())
x = (t - a) * 1000 // 6
h_min = 10 ** 5
for i in range(n):
    if abs(h[i] - x) < h_min:
        h_min = abs(h[i] - x)
        ans = i
print(ans + 1)