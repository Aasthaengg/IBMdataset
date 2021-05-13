import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = sorted(list(map(int, input().split())))

    MAX = max(A) + 1
    flg = [0] * MAX
    tmp = set()
    for a in A:
        if a in tmp:
            flg[a] = 1
        tmp.add(a)

    res = 0
    for a in A:
        if not flg[a]:
            res += 1
        for i in range(a, MAX, a):
            flg[i] = 1
    print(res)


if __name__ == '__main__':
    resolve()
