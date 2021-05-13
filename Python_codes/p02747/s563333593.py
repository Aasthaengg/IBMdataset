import math
import sys
import bisect
readline = sys.stdin.readline


def main():
    s = readline().rstrip()
    print('Yes' if s == 'hi' or s == 'hihi' or s == 'hihihi'or s ==
          'hihihihi' or s == 'hihihihihi' else 'No')


if __name__ == '__main__':
    main()
