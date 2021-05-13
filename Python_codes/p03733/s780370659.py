n, a = map(int, input().split())
t = list(map(int, input().split()))
ans = a
for i in range(1, n):
    ans += min(a, t[i] - t[i - 1])
print(ans)