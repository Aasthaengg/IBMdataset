import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = 10**9

def main():
    S = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    count = 0
    for s in alphabet:
        if s not in S:
            print(s)
            return
        if len(set(alphabet)- set(S)) == 0:
            print(None)
            return


if __name__ == '__main__':
    main()
