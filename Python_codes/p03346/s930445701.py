MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from collections import deque

def main():
    n = int(input())
    idx = [-1] * n
    for i in range(n):
        p = int(input())
        p -= 1
        idx[p] = i
    
    ans = 1
    tmp = 1
    for i in range(1,n):
        if idx[i - 1] < idx[i]:
            tmp += 1
        else:
            ans = max(ans,tmp)
            tmp = 1
    ans = max(ans,tmp)
    print(n - ans)

if __name__ =='__main__':
    main()  
