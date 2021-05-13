# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, A):
    m = ans = 1000
    s = 0
    for i in range(N - 1):
        if A[i + 1] > A[i]:
            s += m // A[i]
            m %= A[i]
        else:
            m += s * A[i]
            s = 0
        ans = max(ans, m)
    ans = max(ans, m + s * A[-1])
    print(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    *A, = map(int, input().split())
    main(N, A)
