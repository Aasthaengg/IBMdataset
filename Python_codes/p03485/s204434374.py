import sys
from math import ceil
def input(): return sys.stdin.readline().strip()


def main():
    a, b = map(int, input().split())
    print(ceil((a + b) / 2))



if __name__ == "__main__":
    main()
