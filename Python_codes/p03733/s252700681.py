n, T = map(int, input().split())
t = list(map(int, input().split()))
ans = T
for i in range(1, n):
    if t[i] >= t[i-1]+T:
        ans += T
    else:
        ans += T - ((t[i-1]+T)-t[i])

print(ans)
