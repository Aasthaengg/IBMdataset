def solve(x, y):
    res = 0
    res += max(0, (4-x) * 10**5)
    res += max(0, (4-y) * 10**5)
    res += 4 * 10**5 * int(x==1 and y==1)
    return res

x, y = map(int, input().split())
print(solve(x, y))