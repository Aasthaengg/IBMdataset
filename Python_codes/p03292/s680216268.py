a = list(map(int, input().split()))
a = sorted(a)
ans = 0
for i in range(1, 3):
    ans += a[i]-a[i-1]
print(ans)
