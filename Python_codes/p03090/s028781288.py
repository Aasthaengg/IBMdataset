import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    res = []
    remove = n
    if n % 2 != 0:
        remove -= 1

    for i in range(n):
        for j in range(i + 1, n):
            if j + 1 == remove:
                continue
            res.append([i + 1, j + 1])
        remove -= 1

    print(len(res))
    for i in res:
        print(*i)


if __name__ == '__main__':
    resolve()
