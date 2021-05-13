MOD = 10 ** 9 + 7
INF = 10 ** 12
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from  itertools import permutations
from heapq import heapify,heappop,heappush

def main():
    n = int(input())
    ans = 0
    for i in range(1,n):
        if i * i > n:
            break
        if n%i == 0:
            j = n//i
            if j - 1 > i:
                ans += j - 1
    print(ans)
    
if __name__ =='__main__':
    main()  