import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y = map(int, input().split())

    if x % y == 0:
        print(-1)
        exit()

    for res in range(x, 10 ** 18, x):
        if res % y:
            print(res)
            break


if __name__ == '__main__':
    resolve()
