import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    n = len(s)

    subss = [""]
    subs = ""
    res = 0
    for i in range(n):
        subs += s[i]
        if subss[-1] != subs:
            subss.append(subs)
            res += 1
            subs = ""

    print(res)


if __name__ == '__main__':
    resolve()
