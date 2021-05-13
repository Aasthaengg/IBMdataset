# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
from math import ceil
def main(N, K, A):
    def cut_times(longest):
        return sum(a // longest for a in A if a > longest)
    under = 0
    r = 10**9
    for i in range(100):
        m = (under + r) / 2
        if cut_times(m) > K: under = m
        else: r = m
    print(ceil(r - 10**-10))

if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = map(int, input().split())
    *A, = map(int, input().split())
    main(N, K, A)
