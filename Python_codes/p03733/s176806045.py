N, T = map(int, input().split())
*t, = map(int, input().split())
ans = 0
last = -10**10
for a in t:
    ans += T - max(last + T - a, 0)
    last = a
print(ans)
