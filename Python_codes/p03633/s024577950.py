def gcd(x: int, y: int) -> int:
    return x if y == 0 else gcd(y, x % y)


def lcm(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)


N = int(input())
T = [int(input()) for _ in range(N)]

ans = 1
for t in T:
    ans = lcm(ans, t)
print(ans)
