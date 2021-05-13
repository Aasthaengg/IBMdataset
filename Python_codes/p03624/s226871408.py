import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = 10**9

def main():
    S = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    S_set = set(S)
    alphabet_set = set(alphabet)

    array = list(alphabet_set - S_set)
    array.sort()
    if len(array) == 0:
        print('None')
    else:
        print(array[0])


if __name__ == '__main__':
    main()
