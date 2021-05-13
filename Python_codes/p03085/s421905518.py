import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    b = input()

    if b == "A":
        print("T")
    elif b == "T":
        print("A")
    elif b == "C":
        print("G")
    else:
        print("C")


if __name__ == '__main__':
    resolve()
