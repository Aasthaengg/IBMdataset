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
    n=I()
    counta=0
    countb=0
    countab=0
    ans=0
    for i in range(n):
        s=SI()
        if s[-1]=="A":
            if s[0]=="B":
                countab+=1
            else:
                counta+=1
        else:
            if s[0]=="B":
                countb+=1
        for i in range(len(s)-1):
            if s[i]=="A" and s[i+1]=="B":
                ans+=1
    if counta>0 and countb>0:
        ans+=countab+1
        counta-=1
        countb-=1
        ans+=min(counta,countb)
    elif counta>0:
        ans+=countab
    elif countb>0:
        ans+=countab
    else:
        ans+=max(0,countab-1)
    print(ans)
                

            
        








if __name__=="__main__":
    main()
