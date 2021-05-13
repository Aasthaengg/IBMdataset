def ceil(a, b):
    return (a + b - 1) // b


N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = sum(b) - sum(a)
for _a, _b in zip(a, b):
    if _a < _b:
        n -= ceil(_b - _a, 2)
if n >= 0:
    print('Yes')
else:
    print('No')
