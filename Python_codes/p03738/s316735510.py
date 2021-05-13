import sys
from collections import Counter
readline = sys.stdin.buffer.readline
MOD = 10**9+7

def main():
    A = int(readline())
    B = int(readline())
    if A>B:
        print('GREATER')
    elif A<B:
        print('LESS')
    else:
        print('EQUAL')




if __name__ == '__main__':
    main()