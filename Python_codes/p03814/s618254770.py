import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()

    idx_a = s.index("A")
    idx_z = -1

    for i, char in enumerate(s):
        if char == "Z":
            idx_z = i

    print(idx_z - idx_a + 1)


if __name__ == '__main__':
    main()
