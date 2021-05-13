import sys

A, B, C = map(int, input().split())
i = 1
while (A*i)%B != C:
    i += 1
    if i > 100:
        print('NO')
        sys.exit()
print('YES')
