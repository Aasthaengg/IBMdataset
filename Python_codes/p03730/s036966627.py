# from pprint import pprint
# import math
# import collections

# n = int(input())
a, b, c = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))

s = 0
mods = []
while True:
    s += a

    mod = s % b

    if mod == c:
        res = 'YES'
        break
    elif mod in mods:
        res = 'NO'
        break

    mods.append(mod)

print(res)
