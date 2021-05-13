import sys
mod = 7 + 10 ** 9

def lcm(a, b):
    a, b = max(a, b), min(a, b)
    c = a * b
    while a % b > 0:
        a, b = b, a % b
    return c // b

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().split()]
    L = A[0]
    for i in range(1, N): L = lcm(L, A[i])
    L %= mod
    ans = 0
    for a in A:
        ans += (L * pow(a, mod - 2, mod)) % mod
        ans %= mod
    print(ans)

    return 0

if __name__ == "__main__":
    solve()