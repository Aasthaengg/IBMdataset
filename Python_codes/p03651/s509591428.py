import fractions
import functools

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, K = ZZ()
    A = ZZ()
    g = functools.reduce(fractions.gcd, A)
    print('POSSIBLE' if K <= max(A) and K%g == 0 else 'IMPOSSIBLE')
    return

if __name__ == '__main__':
    main()

