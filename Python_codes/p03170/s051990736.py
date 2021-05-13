import sys
sys.setrecursionlimit(10 ** 6)


def main():
    N, K = map(int, input().split())
    A = tuple(sorted(map(int, input().split())))
    c = [0] * (K + 1)
    def dp(k, A, c, turn):
        if c[k] != 0:
            return c[k] * turn
        for i in A:
            if i > k:
                break
            if dp(k - i, A, c, -turn) == turn:
                c[k] = 1
                return turn
        c[k] = -1
        return -turn
    
    print('First' if dp(K, A, c, 1) == 1 else 'Second')


main()
