def answer(n, c, k, ts):
    ts.sort()
    bus = 1
    _c = 1
    standard = ts[0]
    for i in range(1, len(ts)):
        if ts[i] <= standard+k and _c < c:
            _c += 1
        else:
            _c = 1
            standard = ts[i]
            bus += 1
    return bus
    
n, c, k = map(int, input().split())
ts = []
for _ in range(n):
    ts.append(int(input()))
print(answer(n, c, k, ts))