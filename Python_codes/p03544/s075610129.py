import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    pre = 2
    now = 1
    for _ in range(n):
        pre, now = now, now + pre
    print(pre)


if __name__ == "__main__":
    main()
