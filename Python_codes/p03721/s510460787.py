import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *AB = map(int, read().split())
    vec = [0] * (10 ** 5 + 1)
    for a, b in zip(*[iter(AB)] * 2):
        vec[a] += b

    total = 0
    for i, n in enumerate(vec):
        total += n
        if total >= K:
            ans = i
            break

    print(ans)
    return


if __name__ == '__main__':
    main()
