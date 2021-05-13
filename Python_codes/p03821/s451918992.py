import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    AB = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for i in reversed(range(n)):
        a, b = AB[i]
        a += res
        if a % b != 0:
            res += (a // b + 1) * b - a
    print(res)


if __name__ == '__main__':
    resolve()
