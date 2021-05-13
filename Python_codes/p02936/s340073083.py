import copy
import math
import time
import statistics
import math
import itertools
import bisect
import sys
from decimal import *

# a = get_int()
def get_int():
    return int(input())
# a = get_string()
def get_string():
    return input()
# a_list = get_int_list()
def get_int_list():
    return [int(x) for x in input().split()]
# a_list = get_string_list():
def get_string_list():
    return input().split()
# a, b = get_int_multi()
def get_int_multi():
    return map(int, input().split())
# a_list = get_string_char_list()
def get_string_char_list():
    return list(str(input()))
# print("{} {}".format(a, b))
# for num in range(0, a):
# a_list[idx]
# a_list = [0] * a
'''
while (idx < n) and ():

    idx += 1
'''

def main():

    start = time.time()

    n, q = get_int_multi()

    a = [[] for _ in range(n+1)]
    for _ in range(n-1):
        s, e = get_int_multi()
        a[s].append(e)
        a[e].append(s)

    point = [0] * (n+1)
    for _ in range(q):
        p, x = get_int_multi()
        point[p] += x

    def tasu(now, prev):
        for next in a[now]:
            if next == prev:
                continue
            point[next] += point[now]
            tasu(next, now)

    sys.setrecursionlimit(10 ** 6)
    tasu(1, -1)
    point = point[1:] #１つ目は0なので除去（inputは1始まりなので、0は使わない）
    print(*point) # * は引数展開　listの中身を引数にする。例えばprint(*[1,2,3])はprint(1,2,3)になり 1 2 3 が出力される


if __name__ == '__main__':
    main()


