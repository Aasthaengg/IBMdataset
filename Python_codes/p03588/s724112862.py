def solve(n, a, b):
    return sum(sorted(zip(a, b)).pop())

n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
print(solve(n, a, b))