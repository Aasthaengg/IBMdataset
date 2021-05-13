ab = [0]*4
for _ in range(3):
    a, b = map(int, input().split())
    ab[a-1] += 1
    ab[b-1] += 1

if max(ab) >= 3:
    print('NO')
else:
    print('YES')
