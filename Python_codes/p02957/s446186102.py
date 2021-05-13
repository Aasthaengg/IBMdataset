#from math import gcd

from math import factorial as f

from math import ceil,floor,sqrt


import bisect
import re
import heapq


from copy import deepcopy
import itertools

from sys import exit

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

yes = "Yes"
no = "No"

def main():
    a,b = mi()
    if a%2 != b%2:
        print('IMPOSSIBLE')
        exit()
    else:
        print((a+b)//2)

main()


