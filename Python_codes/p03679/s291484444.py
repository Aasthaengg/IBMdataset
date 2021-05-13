import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, a, b = map(int, input().split())
    late = a - b
    if late >= 0:
        print("delicious")
    else:
        if x + late >= 0:
            print("safe")
        else:
            print("dangerous")


if __name__ == '__main__':
    resolve()
