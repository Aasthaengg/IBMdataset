import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    b = input()
    res = {"A": "T", "T": "A", "C": "G", "G": "C"}

    print(res[b])

if __name__ == '__main__':
    main()
