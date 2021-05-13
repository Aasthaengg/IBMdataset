# -*- coding: utf-8 -*-

s = input()

head = s[:2]
tail = s[2:]

result = ['MMYY', 'YYMM', 'AMBIGUOUS', 'NA']
judge = [0, 0]
months = [f'{m:02}' for m in range(1, 13)]
if head in months:
    judge[0] += 1
if tail in months:

    judge[1] += 1


if sum(judge) == 2:
    print(result[2])

elif sum(judge) == 0:
    print(result[3])
else:
    print(result[judge.index(1)])
