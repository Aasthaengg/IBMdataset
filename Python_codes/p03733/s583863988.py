n, T = map(int, input().split())
t = list(map(int, input().split()))
ans = 0
tmp = t[0]
for i in range(1, n):
    if t[i] > t[i-1] + T:
        ans += t[i-1] - tmp + T
        tmp = t[i]
ans += t[n-1] - tmp + T
print(ans)