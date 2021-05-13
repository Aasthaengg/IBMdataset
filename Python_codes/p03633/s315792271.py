import sys
from math import gcd
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    ans = int(input())
    for _ in range(n - 1):
        val = int(input())
        ans = ans * val // gcd(ans, val)
    print(ans)

if __name__ == "__main__":
    main()
