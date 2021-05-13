def solve(m1, d1, m2, d2):
    return int(m1 != m2)

m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())
print(solve(m1, d1, m2, d2))