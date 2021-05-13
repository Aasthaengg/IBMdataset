import sys
from functools import lru_cache
def input(): return sys.stdin.readline().strip()


def main():
    n = input()
    ans = ""
    for i in n:
        if i == '1': ans += '9'
        if i == '9': ans += '1'
    print(int(ans))



if __name__ == "__main__":
    main()
