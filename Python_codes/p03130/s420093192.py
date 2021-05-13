c = [0]*4

for i in range(3):
    a, b = map(int, input().split())
    c[a-1] += 1
    c[b-1] += 1

if sorted(c) == [1, 1, 2, 2]:
    print('YES')
else:
    print('NO')
