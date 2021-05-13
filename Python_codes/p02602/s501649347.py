# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, K, A):
    for i in range(K, N):
        print('Yes' if A[i] > A[i - K] else 'No')

if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = map(int, input().split())
    *A, = map(int, input().split())
    main(N, K, A)
