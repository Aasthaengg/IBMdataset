import sys
import re
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


# def main():
#     S = input()

#     ans = 0
#     res = re.findall(r'A*ABC(?:A|BC)*', S)
#     for r in res:
#         r = re.sub(r'(BC)', 'X', r)
#         cnt = 0
#         for c in r[::-1]:
#             if c == 'X':
#                 cnt += 1
#             else:
#                 ans += cnt

#     print(ans)


def main():
    S = input()

    S = re.sub(r'(BC)', 'X', S)

    ans = 0
    cnt = 0
    for s in S[::-1]:
        if s == 'X':
            cnt += 1
        elif s == 'A':
            ans += cnt
        else:
            cnt = 0

    print(ans)


if __name__ == '__main__':
    main()
