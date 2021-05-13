def solve(n, a):
    for i in range(n):
        if a[i] % 2 == 1:
            return "first"
    return "second"

n = int(input())
a = [int(input()) for i in range(n)]
print(solve(n, a))