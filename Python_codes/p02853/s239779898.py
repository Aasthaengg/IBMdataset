def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil,pi,factorial
    from operator import itemgetter
    def I(): return int(input())
    def MI(): return map(int, input().split())
    def LI(): return list(map(int, input().split()))
    def LI2(): return [int(input()) for i in range(n)]
    def MXI(): return [[LI()]for i in range(n)]
    def SI(): return input().rstrip()
    def printns(x): print('\n'.join(x))
    def printni(x): print('\n'.join(list(map(str,x))))
    inf = 10**17
    mod = 10**9 + 7
#main code here!
    x,y=MI()
    ans=0
    if x<=3:
        ans+=(4-x)*(10**5)   
    if y<=3:
        ans+=(4-y)*(10**5) 
    if x==1 and y==1:
        ans+=4*10**5
    print(ans)
        
        
        



        
        
        
        
        
    
if __name__=="__main__":
    main()
