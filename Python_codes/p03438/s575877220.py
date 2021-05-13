N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [_b-_a for _a, _b in zip(a, b)]
x, y = 0, 0
for _c in c:
    if _c > 0:
        x += _c//2
    else:
        y -= _c
if x >= y:
    print('Yes')
else:
    print('No')