import collections

n = int(input())
a = list(map(int, input().split(' ')))


def color(rate):
    if 1 <= rate <= 399:
        return 'gray'
    elif 400 <= rate <= 799:
        return 'brown'
    elif 800 <= rate <= 1199:
        return 'green'
    elif 1200 <= rate <= 1599:
        return 'water'
    elif 1600 <= rate <= 1999:
        return 'blue'
    elif 2000 <= rate <= 2399:
        return 'yellow'
    elif 2400 <= rate <= 2799:
        return 'orange'
    elif 2800 <= rate <= 3199:
        return 'red'
    elif 3200 <= rate:
        return 'multi'


MAX_COLORS = 8

l = [color(rate) for rate in a]
c = collections.Counter(l)


k_not_multi = len([k for k in c.keys() if k != 'multi'])
multis = c['multi']

_max = multis + k_not_multi

if k_not_multi == 0:
    _min = 1
else:
    _min = k_not_multi
    # print(k_not_multi)
    #
    # _max = min(k_not_multi + c['multi'], MAX_COLORS)
    #
    # if k_not_multi == 0:
    #     _min = 1
    # else:
    #     _min = k_not_multi
# else:
#     _max = _min = len([k for k in c.keys()])

print(_min, _max)
