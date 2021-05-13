import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b, c, d = map(int, input().split())
    s = input()

    flg = False
    for i in range(a, d):
        if s[i] == "#":
            if s[i + 1] == "#":
                print("No")
                break

        if b - 1 <= i:
            if i + 1 < n:
                if s[i - 1] == s[i] == s[i + 1] == ".":
                    flg = True
    else:
        if c < d:
            print("Yes")
        else:
            if flg:
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    resolve()
