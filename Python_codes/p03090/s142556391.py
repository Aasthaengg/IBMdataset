INF = 10 ** 9
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from  collections import deque

def main():
    n = int(input())
    if n%2 == 0:
        ans = []
        m = n//2
        for i in range(1,m):
            ans.append((i,n - i))
            ans.append((i,i + 1))
            ans.append((i + 1,n - i + 1))
            ans.append((n - i,n - i + 1))
        
        if n > 4:
            ans.append((1,m))
            ans.append((1,m + 1))
            ans.append((m,n))
            ans.append((n,m + 1))
        
        print(len(ans))
        for i in range(len(ans)):
            print(*ans[i])
    
    else:
        if n == 3:
            ans = [[1,3],[2,3]]
            print(2)
            for i in range(2):
                print(*ans[i])
        else:
            ans = []
            m = n//2
            for i in range(1,m):
                ans.append((i,n - i - 1))
                ans.append((i,i + 1))
                ans.append((i + 1,n - i))
                ans.append((n - i,n - i - 1))
            
            ans.append((m,n))
            ans.append((m + 1,n))
            ans.append((1,n))
            ans.append((n,n - 1))

            print(len(ans))
            for i in range(len(ans)):
                print(*ans[i])

if __name__ == '__main__':
    main()
