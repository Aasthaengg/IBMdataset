path = [0 for _ in range(4)]
for _ in range(3):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    path[a] += 1
    path[b] += 1
ans = 0
for i in range(4):
    if path[i] % 2 == 1:
        ans += 1
if ans ==  2:
    print('YES')
else:
    print('NO')