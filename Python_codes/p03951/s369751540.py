import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    s = input()
    t = input()

    for i in range(n + 1):
        flag = True
        for j in range(n - i):
            if s[i + j] != t[j]:
                flag = False
                break
        if flag:
            return print(n + i)


if __name__ == '__main__':
    main()
