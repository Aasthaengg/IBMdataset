n = int(input())
a = list(map(int, input().split()))

s = 0
cnt = 0
for i in range(n):
    s += a[i]
    if i % 2 == 0:
        if s <= 0:
            cnt += abs(s) + 1
            s = 1
    else:
        if s >= 0:
            cnt += abs(s) + 1
            s = -1
ans1 = cnt

s = 0
cnt = 0
for i in range(n):
    s += a[i]
    if i % 2 != 0:
        if s <= 0:
            cnt += abs(s) + 1
            s = 1
    else:
        if s >= 0:
            cnt += abs(s) + 1
            s = -1
ans2 = cnt

print(min(ans1, ans2))
