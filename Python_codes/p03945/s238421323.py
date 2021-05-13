import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    n = len(s)
    res = 0
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
