import sys
from functools import lru_cache
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    for i in range(1, 10):
        if n <= 111 * i:
            print(111 * i)
            return 



if __name__ == "__main__":
    main()
