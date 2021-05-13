import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, K = map(int, readline().split())
    L = list(map(int, readline().split()))
    L.sort(reverse=True)
    ans = 0
    for l in L[:K]:
        ans += l
    print(ans)


if __name__ == '__main__':
    main()
