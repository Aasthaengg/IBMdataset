# from pprint import pprint
# import math
# import collections

n = int(input())
# n, k = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))
s = []
for i in range(n):
    s.append(int(input()))


# 全問正解の場合から低い順に引いていく
tensu = sum(s)

s2 = sorted(s)

tensu_ans = 0

if tensu % 10 == 0:
    if all([True if _s % 10 == 0 else False for _s in s]):
        tensu_ans = 0
    else:
        tensu_ans = tensu - min([_s for _s in s if _s % 10 != 0])
else:
    tensu_ans = tensu

print(tensu_ans)