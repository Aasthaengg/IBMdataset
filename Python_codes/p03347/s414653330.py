MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from collections import deque

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]

    if a[0] != 0:
        print(-1)
        return
    
    ans = a[-1]
    down = a[-1]
    stair = a[-1]
    for i in range(n - 2,-1,-1):
        down -= 1
        stair -= 1
        if down > a[i]:
            print(-1)
            return
        if stair == a[i]:
            continue
        down = max(down,a[i])
        stair = a[i]
        ans += stair
    
    print(ans)

if __name__ =='__main__':
    main()  
