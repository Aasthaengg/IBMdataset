x, y = map(int, input().split())
def a(n):
    if n == 1:
        return 100000 * 3
    if n == 2:
        return 100000 * 2
    if n == 3:
        return 100000
    return 0
res = a(x) + a(y)
if x == y == 1:
    res += 100000*4
print(res)