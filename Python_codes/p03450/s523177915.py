import sys
input = sys.stdin.readline
INF = 10 ** 9
MOD = 10 ** 9 + 7
from collections import deque
sys.setrecursionlimit(100000000)

def main(): 
    n,m = map(int,input().split())
    L = [[] for _ in range(n)]
    R = [[] for _ in range(n)]
    for _ in range(m):
        l,r,d = map(int,input().split())
        l -= 1
        r -= 1
        L[l].append((r,d))
        R[r].append((l,d))
    
    visited = [True] * n
    X = [0] * n

    def dfs(i):
        ans = True
        for r in L[i]:
            j, d = r
            if visited[j]:
                X[j] = X[i] + d
                visited[j] = False
                ans = (ans&dfs(j)) 
            else:
                if X[j] - X[i] != d:
                    ans = False
                    break
        for l in R[i]:
            j,d = l
            if visited[j]:
                X[j] = X[i] - d
                visited[j] = False
                ans = (ans&dfs(j))
            else:
                if X[i] - X[j] != d:
                    ans = False
                    break
        return ans
    
    ans = True
    for i in range(n):
        if visited[i]:
            visited[i] = False
            ans = (ans&dfs(i))
    
    if ans:
        print('Yes')
    else:
        print('No')        
  
if __name__=='__main__':
    main()