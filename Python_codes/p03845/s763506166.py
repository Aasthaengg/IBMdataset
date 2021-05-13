import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    T = list(map(int, readline().split()))
    M, *PX = map(int, read().split())

    s = sum(T)
    ans = [0] * M
    for i, (p, x) in enumerate(zip(*[iter(PX)] * 2)):
        p -= 1
        ans[i] = s + (x - T[p])

    print(*ans, sep='\n')

    return


if __name__ == '__main__':
    main()
