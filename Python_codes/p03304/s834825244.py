INF = 10 ** 9
MOD = 10 **9 + 7
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from heapq import heapify,heappop,heappush

def main():
    n,m,d = map(int,input().split())
    if d == 0:
        ans = (n - d)*(m - 1)/pow(n,2)
    else:
        ans = 2*(n - d)*(m - 1)/pow(n,2)
    print(ans)
if __name__=='__main__':
    main()