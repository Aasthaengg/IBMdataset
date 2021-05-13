n, a, b = map(int, input().split())
ans = 0
tmp = 0
frag10000 = 0
frag1000 = 0
frag100 = 0
frag10 = 0
frag1 = 0
for i in range(n + 1):
    tmp = i
    frag10000 = int(tmp / 10000)
    tmp %= 10000
    frag1000 = int(tmp / 1000)
    tmp %= 1000
    frag100 = int(tmp / 100)
    tmp %= 100
    frag10 = int(tmp / 10)
    tmp %= 10
    frag1 = int(tmp)
    tmp = frag10000 + frag1000 + frag100 + frag10 + frag1
    if a <= tmp <= b:
        ans += i
print(ans)
