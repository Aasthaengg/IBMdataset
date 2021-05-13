n = int(input())
a = list(map(int, input().split()))

res1 = 0
S = 0
# 偶数番目のとき正
for i in range(n):
    S += a[i]
    if i % 2 == 0:
        if S <= 0:
            res1 += abs(1 - S)
            S = 1
    else:
        if S >= 0:
            res1 += abs(-1 - S)
            S = -1

res2 = 0
S = 0
for i in range(n):
    S += a[i]
    if i % 2 == 1:
        if S <= 0:
            res2 += abs(1 - S)
            S = 1
    else:
        if S >= 0:
            res2 += abs(-1 - S)
            S = -1

print(min(res1, res2))
