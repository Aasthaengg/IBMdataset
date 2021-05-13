from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools


import queue
from collections import deque




def main():
    s = input()
    t = 'CODEFESTIVAL2016'
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    print(ans)



if __name__ == '__main__':
    main()

