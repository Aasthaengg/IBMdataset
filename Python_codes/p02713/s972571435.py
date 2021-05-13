#!/usr/bin/env python3
def main():
    from itertools import product
    import math

    K = int(input())

    ans = 0
    for a, b, c in product(range(1, K + 1), repeat=3):
        ans += math.gcd(math.gcd(a, b), c)
    print(ans)


if __name__ == '__main__':
    main()
