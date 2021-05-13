def solve(n, a):
    b = sum(a) / n
    ans = 0
    best = abs(a[0] - b)
    for i in range(n):
        c = abs(a[i] - b)
        if c < best:
            ans, best = i, c
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))