import sys
from collections import defaultdict, deque, Counter
#from bisect import bisect_left
#import heapq
#import math
#import numpy as np

stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)
MIN = -10 ** 9
MOD = 10 ** 9 + 7
INF = float("inf")
IINF = 10 ** 18

n = int(stdin.readline().rstrip())
a = list(map(int, stdin.readline().rstrip().split()))
#A, B, C = map(int, stdin.readline().rstrip().split())
#S = [list(stdin.buffer.readline().decode().rstrip()) for _ in range(h)]

check = set(a)
coll = Counter(a)

if check == {0}:
    print("Yes")
elif len(check) == 3:
    if list(check)[0] ^ list(check)[1] ^ list(check)[2] == 0:
        if coll[list(check)[0]] == coll[list(check)[1]] == coll[list(check)[2]]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
elif len(list(check)) == 2:
    if list(check)[0] == 0:
        if coll[list(check)[0]] * 3 == n:
            print("Yes")
        else:
            print("No")
    elif list(check)[1] == 0:
        if coll[list(check)[0]] * 3 == n:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
