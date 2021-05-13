#!/usr/bin/env python3
import copy

n = int(input())
am = list(map(int, input().split()))

pcnt = 0
mcnt = 0

f = 0  #前の項の符号（1:+、2:-）
wa = 0

#最初の数字を正とするとき
a = copy.copy(am)
f = 2

for i in range(n):
    wa += a[i]

    if f == 1:#-にする必要あり
        if wa > -1:
            pcnt += wa + 1
            wa = -1
        
        f = 2

    elif f == 2:  #+にする必要あり

        if wa < 1:
            pcnt += -wa + 1
            wa = 1

        f = 1

#最初の数字を負とするとき
a = copy.copy(am)
wa = 0
f = 1

for i in range(n):
    wa += a[i]

    if f == 1:  # -にする必要あり
        if wa > -1:
            mcnt += wa + 1
            wa = -1

        f = 2

    elif f == 2:  # +にする必要あり

        if wa < 1:
            mcnt += -wa + 1
            wa = 1

        f = 1

print(min(pcnt, mcnt))
