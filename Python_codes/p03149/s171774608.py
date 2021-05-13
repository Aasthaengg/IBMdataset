# import math
# import decimal
# import queue
# import bisect
# import heapq
# import time
# import itertools

mod = int(1e9+7)

def main():
    n = list(map(int,input().split()))
    n.sort()
    if n[0] == 1 and n[1] == 4 and n[2] == 7 and n[3] == 9:
        print('YES')
    else:
        print('NO')
    return

if __name__=='__main__':
    main()
