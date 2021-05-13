from itertools import chain


def cost(p1, p2):
    return abs(p1 - p2)


input()
points = tuple(chain.from_iterable(([0], tuple(map(int, input().split(' '))), [0])))

base_cost = sum([cost(p, pre_p) for pre_p, p in zip(points, points[1:])])

for pre_p, p, next_p in zip(points, points[1:], points[2:]):
    diff = cost(pre_p, next_p) - cost(pre_p, p) - cost(p, next_p)
    print(base_cost + diff)
