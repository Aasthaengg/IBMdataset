import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, B, C = map(int, readline().split())

    def judge():
        for i in range(0, 100000):
            cur = A * i
            if cur % B == C:
                return True
        return False

    if judge():
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
