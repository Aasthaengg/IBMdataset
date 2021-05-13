import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import product
    x = list(map(int, readline().split()))

    def judge():
        for bit in product(range(2), repeat=3):
            first = 0
            second = 0
            for i, b in enumerate(bit):
                if b:
                    first += x[i]
                else:
                    second += x[i]
            if first == second:
                return True
        return False

    if judge():
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
