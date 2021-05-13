import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, X, *A = map(int, read().split())
    
    v = 0
    for a in A:
        if a < X:
            v += 1
        else:
            break
    
    print(min(v, M - v))
    return


if __name__ == '__main__':
    main()
