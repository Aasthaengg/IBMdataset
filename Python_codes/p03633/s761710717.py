import sys
import fractions

def input(): return sys.stdin.readline().strip()
def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N = Z()
    T = [Z() for _ in range(N)]
    ans = T[0]
    for i in range(1, N):
        g = fractions.gcd(ans, T[i])
        ans *= T[i]
        ans //= g
    print(ans)

    return

if __name__ == '__main__':
    main()
