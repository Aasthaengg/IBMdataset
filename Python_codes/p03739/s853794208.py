n = int(input())
a = list(map(int, input().split()))

# a[0] > 0
ans = 0
if a[0] <= 0:
    ans += -a[0] + 1
    s = 1
else:
    s = a[0]
for i in range(1, n):
    if s > 0:
        s += a[i]
        if s >= 0:
            ans += s + 1
            s = -1
    else:
        s += a[i]
        if s <= 0:
            ans += -s + 1
            s = 1
ans1 = ans

# a[0] < 0
ans = 0
if a[0] >= 0:
    ans += a[0] + 1
    s = -1
else:
    s = a[0]
for i in range(1, n):
    if s > 0:
        s += a[i]
        if s >= 0:
            ans += s + 1
            s = -1
    else:
        s += a[i]
        if s <= 0:
            ans += -s + 1
            s = 1

print(min([ans1, ans]))