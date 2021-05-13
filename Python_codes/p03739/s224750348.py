n = int(input())
a = list(map(int, input().split()))
s = [a[0] for _ in range(n)]
t = [a[0] for _ in range(n)]
for i in range(1, n):
    s[i] = s[i - 1] + a[i]
    t[i] = t[i - 1] + a[i]
x, y = 0, 0
ans1, ans2 = 0, 0
for i in range(n):
    ss = s[i] + x
    tt = t[i] + y
    if i % 2 == 0:
        if ss <= 0:
            x += abs(ss) + 1
            ans1 += abs(ss) + 1
        if tt >= 0:
            y -= abs(tt) + 1
            ans2 += abs(tt) + 1
    else:
        if ss >= 0:
            x -= abs(ss) + 1
            ans1 += abs(ss) + 1
        if tt <= 0:
            y += abs(tt) + 1
            ans2 += abs(tt) + 1
print(min(ans1, ans2))