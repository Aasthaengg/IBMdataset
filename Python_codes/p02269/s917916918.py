from collections import deque, defaultdict
import sys
import math

if __name__ == '__main__':
    n = int(input())
    s = defaultdict(int)
    for _ in range(n):
        a, b = input().split()
        if a == 'insert':
            s[b] += 1
        else:
            if s[b]:
                print('yes')
            else:
                print('no')
