# from pprint import pprint
# import math
# import collections

s = input()
# n = int(input())
# n, k = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))
s_l = list(s)

res = [None] * len(s_l)

for i, _s in enumerate(s_l):
    if _s == 'L' and i > 0:
        # 左がLのLは0
        if s_l[i - 1] == 'L':
            res[i] = 0
        # 左がRのL
        else:
            # print('L/')
            res[i] = 1

            # 左のR
            j = 2
            cnt = 0
            while 0 <= i - j:
                if s_l[i - j] == 'R':
                    if j % 2 == 0:
                        cnt += 1
                else:
                    break
                j += 1
            # print('l_cnt', cnt)
            res[i] += cnt

            # 右のL
            j = 1
            cnt = 0
            while i + j < len(s_l):
                if s_l[i + j] == 'R':
                    break
                else:
                    if j % 2 == 0:
                        cnt += 1
                j += 1
            # print('r_cnt', cnt)
            res[i] += cnt

        # print('L', res[i])

    if _s == 'R' and i < len(s_l) - 1:
        # 右がRのRは0
        if s_l[i + 1] == 'R':
            res[i] = 0
        # 右がLのR
        else:
            # print('R/')
            res[i] = 1

            # 左のR
            j = 1
            cnt = 0
            while 0 <= i - j:
                if s_l[i - j] == 'L':
                    break
                else:
                    if j % 2 == 0:
                        cnt += 1
                j += 1
            # print('l_cnt', cnt)
            res[i] += cnt

            # 右のL
            j = 2
            cnt = 0
            while i + j < len(s_l):
                if s_l[i + j] == 'L':
                    if j % 2 == 0:
                        cnt += 1
                else:
                    break
                j += 1
            # print('r_cnt', cnt)
            res[i] += cnt

        # print('R', res[i])

res = [str(r) for r in res]

print(' '.join(res))
