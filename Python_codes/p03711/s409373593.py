x, y = map(int, input().split())

groups = (
    frozenset([1, 3, 5, 7, 8, 10, 12]),
    frozenset([4, 6, 9, 11]),
    frozenset([2])
    )

for group in groups:
    if x in group and y in group:
        print('Yes')
        break
else:
    print('No')
