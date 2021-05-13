# coding = SJIS

k, s = map(int, input().split())
ans = 0

if s < k:
    ans = (s + 1) * (s + 2) / 2
elif s <= 2 * k:
    t = 2 * k - s
    a = (k + 1) * (k + 2) / 2
    b = t * (t + 1) / 2
    c = t * (2 * k - (t - 1)) / 2
    ans = a - b + c
elif s <= 3 * k:
    t = 3 * k - s + 1
    ans = t * (t + 1) / 2
print(int(ans))