import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    ab, bc, ca = map(int, input().split())
    res = (ab * bc) // 2
    print(res)


if __name__ == '__main__':
    resolve()
