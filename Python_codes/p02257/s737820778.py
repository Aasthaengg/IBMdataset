import sys

def solve():
    n = int(sys.stdin.readline())

    ans = sum(is_prime(int(sys.stdin.readline())) for i in range(n))

    print(ans)

def is_prime(n):
    if n < 2 or (n > 2 and n & 1 == 0):
        return False

    p = 3

    while p*p <= n:
        if n % p == 0:
            return False

        p += 2

    return True

if __name__ == '__main__':
    solve()