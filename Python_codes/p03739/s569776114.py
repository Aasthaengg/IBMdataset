N = int(input())
A = [int(x) for x in input().split()]


# plusスタートにする
ans1 = 0
c = 0
plus = True
for a in A:
    c += a
    if plus:
        if c <= 0:
            ans1 += abs(c) + 1
            c = 1
        plus = False
    else:
        if c >= 0:
            ans1 += abs(c) + 1
            c = -1
        plus = True

# minusスタートにする
ans2 = 0
c = 0
plus = False
for a in A:
    c += a
    if plus:
        if c <= 0:
            ans2 += abs(c) + 1
            c = 1
        plus = False
    else:
        if c >= 0:
            ans2 += abs(c) + 1
            c = -1
        plus = True

print(min(ans1, ans2))
