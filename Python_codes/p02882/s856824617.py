import sys
import math
from collections import defaultdict, deque, Counter
from copy import deepcopy
from bisect import bisect, bisect_right, bisect_left
from heapq import heapify, heappop, heappush
    
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]
    
    
def main():
    a,b,x = MI()
    a2b = (a**2)*b
    a3 = (a**3)/2
    ab2 = a*(b**2)/2
    
    pai = math.pi/2
    low = 0
    high = math.pi/2
    mid = (low+high)/2
    
    while high - low > 0.0000000000001:
        if a * math.tan(pai-mid) < b:
            v = a2b - a3 * math.tan(pai-mid)
        else:
            v = ab2 * math.tan(mid)
        
        if v < x:
            low = mid
        else:
            high = mid
            
        mid = (low+high)/2

    print(90 - math.degrees(mid))

if __name__ == "__main__":
    main()