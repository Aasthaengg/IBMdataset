T = [0 for _ in range(4)]
for i in range(3):
    a, b = map(int, input().split())
    T[a - 1] += 1
    T[b - 1] += 1
if max(T) == 3:
    print('NO')
else:
    print('YES')