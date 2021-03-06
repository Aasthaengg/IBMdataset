import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input()

    right = 0
    left = 0
    for i in range(n):
        if S[i] == "(":
            left += 1
        else:
            if left:
                left -= 1
            else:
                right += 1
    res = "(" * right + S + ")" * left
    print(res)


if __name__ == '__main__':
    resolve()
