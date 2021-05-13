import math  # noqa
import bisect  # noqa
import queue  # noqa


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]

    cnt = 0
    cnt_xa = 0
    cnt_bx = 0
    cnt_ba = 0
    for s in S:
        for i in range(0, len(s) - 1):
            if s[i] == 'A' and s[i + 1] == 'B':
                cnt += 1
        if 'B' != s[0] and 'A' == s[-1]:
            cnt_xa += 1
        if 'B' == s[0] and 'A' != s[-1]:
            cnt_bx += 1
        if 'B' == s[0] and 'A' == s[-1]:
            cnt_ba += 1

    if cnt_ba > 1:
        cnt += cnt_ba - 1
        cnt_ba = 1
    if (cnt_xa > 0 or cnt_bx > 0) and cnt_ba == 1:
        cnt += 1
    cnt += min(cnt_xa, cnt_bx)

    print(cnt)
