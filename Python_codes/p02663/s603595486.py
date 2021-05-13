def solve(h1, m1, h2, m2, k):
    return (h2-h1)*60 + (m2-m1) - k

h1, m1, h2, m2, k = map(int, input().split())
print(solve(h1, m1, h2, m2, k))