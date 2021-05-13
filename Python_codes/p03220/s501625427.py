n, t, a, *h = map(int, open(0).read().split())
ans = 0
diff_a = float('inf')
for i in range(n):
    if diff_a > abs(a - (t - h[i] * 0.006)):
        ans = i+1
        diff_a = abs(a - (t - h[i] * 0.006))
print(ans)