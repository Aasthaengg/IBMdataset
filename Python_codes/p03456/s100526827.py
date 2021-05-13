import sys
from math import sqrt
def input(): return sys.stdin.readline().strip()


def main():
    a, b = input().split()
    n = int(a + b)
    r = round(sqrt(n))
    if r * r == n:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
