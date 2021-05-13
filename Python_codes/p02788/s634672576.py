from math import * 
import sys
from collections import *
input = sys.stdin.readline

def main():
    N, D, A = list(map(int, input().split()))
    XH = sorted([list(map(int, input().split())) for i in range(N)])

    t = 0
    q = deque([])
    
    ans = 0
    for X, H in XH:
        while q and q[0][0] < X-D:
            x, c = q.popleft()
            
            t -= c
        H -= A * t
        
        if H <= 0: continue 

        c = ceil(H/A)
        ans += c
        q.append((X+D, c))
        t += c   
    print(ans)
if __name__ == '__main__':
    main()
