n = int(input())
a = list(map(int, input().split()))
ans1, ans2 = 0, 0
s = 0
plus = True
for i in range(n):
    if plus:
        if s + a[i] > 0:
            s += a[i]
        else:
            ans1 += abs(1 - (s + a[i]))
            s = 1
    if not plus:
        if s + a[i] < 0:
            s += a[i]
        else:
            ans1 += abs(-1 - (s + a[i]))
            s = -1
    plus = not plus

s = 0
plus = False
for i in range(n):
    if plus:
        if s + a[i] > 0:
            s += a[i]
        else:
            ans2 += abs(1 - (s + a[i]))
            s = 1
    if not plus:
        if s + a[i] < 0:
            s += a[i]
        else:
            ans2 += abs(-1 - (s + a[i]))
            s = -1
    plus = not plus
print(min(ans1, ans2))