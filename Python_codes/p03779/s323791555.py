import sys
from math import ceil
def input(): return sys.stdin.readline().strip()

def main():
    X = int(input())
    val = (1 + 8 * X) ** 0.5 - 1
    print(ceil(val / 2))


if __name__ == "__main__":
    main()
