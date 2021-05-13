import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    N, K = map(int, readline().split())
    K -= 1
    S = readline().strip()
    
    S = list(S)
    S[K] = S[K].lower()
    print(''.join(S))
    return


if __name__ == '__main__':
    main()
