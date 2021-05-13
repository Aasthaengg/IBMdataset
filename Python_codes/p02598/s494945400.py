# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, K, A):
    lo = 0
    hi = 10**9
    while hi - lo > 1:
        m = (lo + hi) // 2
        if sum((a + m - 1) // m - 1 for a in A) <= K: hi = m
        else: lo = m
    print(hi)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = map(int, input().split())
    *A, = map(int, input().split())
    main(N, K, A)
