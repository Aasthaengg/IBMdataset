n, T = map(int, input().split())
*t, = map(int, input().split())
ans = 0
for i, j in zip(t, t[1:]):
    ans += min(T, j-i)
print(ans+T)