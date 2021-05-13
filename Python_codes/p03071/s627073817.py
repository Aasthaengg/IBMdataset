# coding = SJIS
a, b = map(int, input().split())
ans = 0
if a <= b:
    ans += b
    b -= 1
    ans += max(a, b)
else:
    ans += a
    a -= 1
    ans += max(a, b)
print(ans)