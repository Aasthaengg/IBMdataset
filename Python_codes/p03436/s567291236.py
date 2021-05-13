import copy
import math
import time
import statistics
import math
import itertools
import bisect
import sys
from decimal import *
from collections import deque


def get_int():
    return int(input())

def get_string():
    return input()

def get_int_list():
    return [int(x) for x in input().split()]

def get_string_list():
    return input().split()

def get_int_multi():
    return map(int, input().split())

def get_string_char_list():
    return list(str(input()))

# print("{} {}".format(a, b))
# a_list = [0] * a
sys.setrecursionlimit(10 ** 6)

def main():
    start = time.time()

    h, w = get_int_multi()

    d = [[-1] * (w+2) for _ in range(h+2)]

    shiro = 0
    for i in range(h):
        wk = get_string()
        for ii in range(w):
            if wk[ii] == ".":
                d[i+1][ii+1] = 10**9
                shiro += 1


    d[1][1] = 1
    q = deque([])
    q.append([1,1])

    flg = False
    while q:
        wk = q.popleft()
        i = wk[0]
        ii = wk[1]
        hosuu = d[i][ii]

        if i == h and ii == w:
            flg = True
            print(shiro-hosuu)
            break

        def add_que(i,ii,hosuu):
            if d[i][ii] == 10**9:
                d[i][ii] = hosuu + 1
                q.append([i,ii])

        add_que(i-1,ii, hosuu)
        add_que(i+1,ii, hosuu)
        add_que(i,ii-1, hosuu)
        add_que(i,ii+1, hosuu)

    if not flg:
        print(-1)



if __name__ == '__main__':
    main()


