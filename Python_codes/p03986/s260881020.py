import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = input()

    cnt_S = 0
    cnt_T = 0
    res = 0
    i = 0
    while i < len(x):
        if x[i] == "S":
            cnt_S += 1
            i += 1

        elif x[i] == "T" and cnt_S != 0:
            while i < len(x) and x[i] == "T":
                cnt_T += 1
                i += 1
            res += min(cnt_S, cnt_T) * 2
            cnt_S -= min(cnt_S, cnt_T)
            cnt_T = 0
        else:
            i += 1

    print(len(x) - res)


if __name__ == '__main__':
    resolve()
