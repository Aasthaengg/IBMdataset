def solve(a, b, c):
    if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
        return 0
    a, b, c = sorted([a, b, c])
    return a * b


print(solve(*map(int, input().split())))
