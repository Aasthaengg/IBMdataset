# from pprint import pprint
# import math
# import collections

n = int(input())
# n, k = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))
a = []
for i in range(n):
    a.append(int(input()))

l = {}
for _a in a:
    if _a in l:
        l.pop(_a)
    else:
        l.update(
            {_a: True}
        )

print(len(l))
