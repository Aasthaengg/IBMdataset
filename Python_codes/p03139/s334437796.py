def solve(n, a, b):
    return " ".join(map(str, [min(a,b), max(0,a+b-n)]))

n, a, b = map(int, input().split())
print(solve(n, a, b))