# import math
# import decimal
# import queue
# import bisect
# import heapq
# import time
# import itertools

mod = int(1e9+7)
INF = 1<<39

def main():
    s = input()
    if len(s) == 2:
        print(s)
    else:
        t = []
        for i in range(3):
            t.insert(0,s[i])
        print(''.join(t))
    return

if __name__=='__main__':
    main()