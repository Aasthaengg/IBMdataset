# coding = SJIS

w, h, x, y = map(int, input().split())

area = w * h
ans = area / 2
ok = 0

if x == w / 2 and y == h / 2:
    ok = 1

print(ans, ok)