import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    r = int(input())
    if r < 1200: print("ABC")
    elif r < 2800: print("ARC")
    else: print("AGC")

if __name__ == "__main__":
    main()
