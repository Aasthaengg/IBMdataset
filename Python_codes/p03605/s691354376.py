import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = input()

    print("Yes") if "9" in n else print("No")


if __name__ == '__main__':
    resolve()
