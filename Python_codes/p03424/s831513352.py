import sys
from math import ceil
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    S = list(input().split())
    yellow = False
    for c in S:
        if c == 'Y':
            yellow = True
            break
    if yellow: print("Four")
    else: print('Three')

if __name__ == "__main__":
    main()
