import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, k, c = list(map(int, readline().split()))
    s = input()
    day_ealiest = []
    day_latest = []

    rest_day = 0
    work_cnt = 0
    for day, ch in enumerate(s, 1):
        if rest_day <= 0:
            if ch == "o":
                rest_day = c
                day_ealiest.append(day)
                work_cnt += 1
                if work_cnt == k:
                    break
        else:
            rest_day -= 1

    s_reversed = s[::-1]
    rest_day = 0
    work_cnt = 0
    for i, ch in enumerate(s_reversed):
        day = n - i
        if rest_day <= 0:
            if ch == "o":
                rest_day = c
                day_latest.append(day)
                work_cnt += 1
                if work_cnt == k:
                    break
        else:
            rest_day -= 1

    day_latest.reverse()

    res = []
    for de, dl in zip(day_ealiest, day_latest):
        if de == dl:
            res.append(de)

    print(*res, sep="\n")


if __name__ == '__main__':
    main()
