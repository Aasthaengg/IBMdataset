import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    s = S()
    if int(s[:2]) > 12 or int(s[:2]) == 0:
        mmyy = False
    else:
        mmyy = True
    if int(s[2:]) > 12 or int(s[2:]) == 0:
        yymm = False
    else:
        yymm = True
    ans = ''
    if yymm and mmyy:
        ans = 'AMBIGUOUS'
    if yymm and not mmyy:
        ans = 'YYMM'
    if not yymm and mmyy:
        ans = 'MMYY'
    if not yymm and not mmyy:
        ans = 'NA'
    print(ans)
        

main()

