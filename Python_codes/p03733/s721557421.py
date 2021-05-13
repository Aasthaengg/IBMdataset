n,t = map(int, input().split())
T = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if T[i] - T[i-1] <= t:
        ans += T[i] - T[i-1]
    else:
        ans += t
ans += t
print(ans)

