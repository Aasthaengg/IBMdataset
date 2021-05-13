a, b, c = map(int, input().split())

count = 0

for _ in range(1000000):
    
    _a, _am = divmod(a, 2)
    _b, _bm = divmod(b, 2)
    _c, _cm = divmod(c, 2)

    if _am or _bm or _cm:
        print(count)
        break
    elif a == b == c:
        print(-1)
        break
    else:
        a = _b + _c
        b = _a + _c
        c = _a + _b
        count += 1
else:
    print(-1)