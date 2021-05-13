_, *_XL = open(0).read().split()

XL = list(zip(*[map(int, iter(_XL))]*2))

ans = 0
t = -10**10 # 数直線のマイナス方向からスタートする

arms = [(X-L, X+L) for X, L in XL]
arms_sorted = sorted(arms, key=lambda k:k[1])

ans = 0

for s, e in arms_sorted:
    if t <= s:
        t = e
        ans += 1
        
print(ans)