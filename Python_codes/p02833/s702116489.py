n = int(input())

def solve(n):
    if n % 2 == 1:
        return 0
    n //= 2
    ans = 0
    fact = 5
    while n >= 5:
        ans += n // 5
        n //= 5
    return ans

print(solve(n))