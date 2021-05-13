def solve(a, b, c):
    if any(i % 2 == 1 for i in [a, b, c]):
        return 0
    if a == b == c:
        return -1
    a, b, c = (b + c) // 2, (c + a) // 2, (a + b) // 2
    return solve(a, b, c) + 1

a, b, c = map(int, input().split())

print(solve(a, b, c))