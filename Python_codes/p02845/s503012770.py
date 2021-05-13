import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    MOD = 1000000007
    N, *A = map(int, read().split())
    seq = [-1] * 3
    ans = 1
    try:
        for a in A:
            ans = ans * seq.count(a - 1) % MOD
            seq[seq.index(a - 1)] = a
        print(ans)
    except:
        print(0)
        
    return


if __name__ == '__main__':
    main()
