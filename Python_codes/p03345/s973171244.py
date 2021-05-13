import sys
from collections import Counter
readline = sys.stdin.buffer.readline
MOD = 10**9+7

def main():
    A, B, C, K = map(int, readline().split())
    if K&1==0:
        print(A-B)
    else:
        print(B-A)




if __name__ == '__main__':
    main()