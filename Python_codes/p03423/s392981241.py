import sys
from math import ceil
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    print(ceil(n // 3))

if __name__ == "__main__":
    main()
