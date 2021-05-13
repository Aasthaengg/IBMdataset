import sys
from fractions import gcd
def input(): return sys.stdin.readline().strip()


def main():
    T, X = map(int, input().split())
    print(T / X)

if __name__ == "__main__":
    main()
