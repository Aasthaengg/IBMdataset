import sys
import numpy as np
import math  # gcdもあるよ
from collections import deque
from collections import defaultdict
from copy import deepcopy
from itertools import accumulate #リストを与えると累積和を返す
def input(): return sys.stdin.readline().rstrip()
from functools import lru_cache #メモ化

def main():
    N = list(map(int,input().split()))
    A1 = N[0] * N[1]
    ans = N[2]
    if A1 < ans:
        print(A1)
    else: print(ans)
    return 0

if __name__ == "__main__":
    main()