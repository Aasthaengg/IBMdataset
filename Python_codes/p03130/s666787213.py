L = []
for _ in range(3):
    x, y = map(int, input().split())
    L.append(x)
    L.append(y)

num = []
num.append(L.count(1))
num.append(L.count(2))
num.append(L.count(3))
num.append(L.count(4))

if max(num) == 3:
    print('NO')
else:
    print('YES')