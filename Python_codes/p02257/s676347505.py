import sys
from math import sqrt

def solve():
    n = int(sys.stdin.readline())

    ans = sum(is_prime(int(sys.stdin.readline())) for i in range(n))

    print(ans)

def is_prime(n):
    if n < 2 or (n > 2 and not(n & 1)):
        return False

    lim = int(sqrt(n)) + 1

    for p in range(3, lim, 2):
        if not(n % p):
            return False
            
    return True

if __name__ == '__main__':
    solve()