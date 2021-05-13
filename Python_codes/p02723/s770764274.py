import math
import sys
readline = sys.stdin.readline


def main():
    s = readline().rstrip()
    print('YNeos'[not(s[2] == s[3] and s[4] == s[5])::2])


if __name__ == '__main__':
    main()
