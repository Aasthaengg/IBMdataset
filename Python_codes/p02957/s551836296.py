a, b = map(int, input().split())
x = min(a, b)
y = max(a, b)
k = (y - x)//2 + x
if abs(a-k) == abs(b-k):
    print(k)
else:
    print('IMPOSSIBLE')
