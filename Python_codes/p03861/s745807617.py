# from pprint import pprint
# import math
# import collections

# n = int(input())
a, b, x = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))

_a = a // x + 1
_b = b // x + 1

if a % x == 0:
    _c = 1
else:
    _c = 0

ans = _b - _a + _c

# print(_a, _b, _c, ans)
print(ans)
