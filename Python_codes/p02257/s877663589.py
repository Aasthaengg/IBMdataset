import sys

def solve():
    n = int(sys.stdin.readline())

    ans = sum(is_prime(int(sys.stdin.readline())) for i in range(n))

    print(ans)

def is_prime(n):
    if n < 2:
        return False

    p = 2

    while p*p <= n:
        if n % p == 0:
            return False

        p += 1

    return True

if __name__ == '__main__':
    solve()