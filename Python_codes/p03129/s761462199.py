import sys
# import math
# import decimal
# import queue
# import bisect
# import heapq
import time
# import itertools

mod = int(1e9+7)
INF = 1<<29

def main():
    n,k = map(int,input().split())
    if (n + 1) // 2 >= k:
        print("YES")
    else:
        print("NO")
    return

if __name__=='__main__':
    main()