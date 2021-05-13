import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    X = 0
    AB = []
    for _ in range(N):
        A, B = map(int, readline().split())
        X -= B
        AB.append(A + B)
    AB.sort(reverse=True)
    for ab in AB[::2]:
        X += ab
    print(X)


if __name__ == '__main__':
    main()
