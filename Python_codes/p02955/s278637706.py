import sys,os,math
from collections import Counter, defaultdict, deque
import bisect
from sys import stdin, stdout
from itertools import repeat
import Queue



# n, k = map(int, raw_input().split())
# da = map(int, raw_input().split())
# db = map(int, raw_input().split())


def main():
    n, k = map(int, raw_input().split())
    da = map(int, raw_input().split())
    sm = sum(da)
    mx = max(da)
    ans = 1
    for i in range(1, int(math.sqrt(sm))+1):
        if sm%i==0:
            def check(p):
                l = []
                for num in da:
                    l.append(num%p)
                ssm = n*p - sum(l)
                l.sort()
                ps = 0
                uk = 0
                for num in l:
                    uk += num
                    ssm -= p-num
                    if ssm == uk and uk <= k:
                        return True
                return False
            # print check(7), 7777777
            if check(i):
                ans = max(ans, i)
            if check(sm/i):
                ans = max(ans, sm/i)

    print ans






main()
