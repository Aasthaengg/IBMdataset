x, y, z = map(int, input().split())
i = x + y + z
if i - max(x, y, z) == max(x, y, z) and i % 2 == 0:
    print('Yes')
else:
    print('No')
