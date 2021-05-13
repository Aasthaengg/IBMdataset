import math
import sys
from collections import Counter
readline = sys.stdin.readline


def main():
    s = readline().rstrip()
    t = readline().rstrip()
    cnt = 0
    for k in range(len(s)):
        cnt += 1 if s[k] != t[k] else 0
    print(cnt)


if __name__ == '__main__':
    main()
