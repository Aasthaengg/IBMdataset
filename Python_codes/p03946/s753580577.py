N, T = map(int, input().split())
*a, = map(int, input().split())
m = a[0]
p = 0
ans = 0
for i in range(1, N):
    c = a[i] - m
    if a[i] < m:
        m = a[i]
    if c > p:
        p = c
        ans = 1
    elif c == p:
        ans += 1

print(ans)
