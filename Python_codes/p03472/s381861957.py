n, h = map(int, input().split())
a, b = [], []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai), b.append(bi)
a.sort(), b.sort()

ans, amax = 0, a[-1]
for bi in b[::-1]:
    if bi <= amax:
        print(ans + h // amax + (h % amax > 0))
        break
    if h <= 0:
        print(ans)
        break
    h -= bi
    ans += 1
else:
    print(ans + h // amax + (h % amax > 0))
