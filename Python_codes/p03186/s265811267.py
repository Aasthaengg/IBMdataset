def solve(a, b, c):
    return min(a+b+1, c) + b

a, b, c = map(int, input().split())
print(solve(a, b, c))
