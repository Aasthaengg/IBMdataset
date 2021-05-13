# coding = SJIS
k, s = map(int, input().split())
if s < k:
    ans = (s + 1) * (s + 2) / 2
elif s <= 2 * k:
    t = 2 * k - s
    ans = ((k + 1) * (k + 2) / 2) - ((2 * k - s) * ((2 * k - s) + 1) / 2) + (t * (2 * k - ((2 * k - s) - 1)) / 2)
elif s <= 3 * k:
    ans = (3 * k - s + 1) * ((3 * k - s + 1) + 1) / 2
print(int(ans))