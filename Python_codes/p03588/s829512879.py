import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    AB = list(list(map(int, readline().split())) for _ in range(N))
    ans = max(AB)[0] + max(AB)[1]
    print(ans)

if __name__ == '__main__':
    main()
