# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, K, A, F):
    A.sort()
    F.sort(reverse=True)

    def k(max_t):
        res = 0
        for a, f in zip(A, F):
            t = a * f
            if t > max_t:
                r = t - max_t
                res += (r + f - 1) // f
        return res

    l = -1
    r = 10**12
    while r - l > 1:
        m = (l + r) // 2
        if k(m) <= K: r = m
        else: l = m
    print(r)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = map(int, input().split())
    *A, = map(int, input().split())
    *F, = map(int, input().split())
    main(N, K, A, F)
