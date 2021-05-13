def ceil(a, b):
    return (a + b - 1) // b


N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = sum(b) - sum(a)
cnt = 0
for _a, _b in zip(a, b):
    if _a < _b:
        cnt += ceil(_b - _a, 2)
if cnt <= n:
    print('Yes')
else:
    print('No')
