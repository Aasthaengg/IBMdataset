n = int(input())
a = list(map(int, input().split()))
print(2 * n - 2)
if abs(min(a)) <= abs(max(a)):
    x = a.index(max(a)) + 1
    for y in range(1, n + 1):
        if not x == y:
            print(x, y)
    for x in range(1, n):
        y = x + 1
        print(x, y)
else:
    x = a.index(min(a)) + 1
    for y in range(1, n + 1):
        if not x == y:
            print(x, y)
    for x in range(n, 1, -1):
        y = x - 1
        print(x, y)