N = int(input())
t, x, y = 0, 0, 0
ans = 'Yes'
for _ in range(N):
    tn, xn, yn = map(int, input().split())
    d = abs(xn - x) + abs(yn - y)
    td = tn - t
    if d > td or (d - td)%2 != 0:
        ans = 'No'
    t, x, y = tn, xn, yn
print(ans)