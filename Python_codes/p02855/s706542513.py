def main():
    import sys
    import numpy as np
    sys.setrecursionlimit(10**6)

    def input(): return sys.stdin.readline().rstrip()
        
    def dfs(upper, lower, left, right, cnt):
        
        if cnt == 1:
            ans[upper:lower, left:right] = np.max(ans[upper:lower, left:right])
            return

        elif cnt != max(cntrow[upper:lower]):
            for i in range(upper, lower):
                if cntrow[i]:
                    ncnt = sum(cntrow[upper:i+1])
                    dfs(upper, i+1, left, right, ncnt)
                    dfs(i+1, lower, left, right, cnt-ncnt)
                    break
            
        else:
            idx = cntrow[upper:lower].index(cnt)+upper
            for j in range(left, right):
                if g[idx][j] == '#':
                    dfs(upper, lower, left, j+1, 1)
                    cntrow[idx] -=1
                    dfs(upper, lower, j+1, right, cnt-1)
                    break

      
    h, w, k = map(int, input().split())
    g = ['']*h
    ans = np.zeros(shape=(h, w), dtype=int)
    cnt = 1
    cntrow = [0]*h
    for i in range(h):
        g[i] = input()
        for j in range(w):
            if g[i][j] == '#':
                ans[i, j] = cnt
                cntrow[i] += 1
                cnt += 1
    dfs(0, h, 0, w, k)
    for i in range(h):
        print(*ans[i])

        
        
if __name__ == '__main__':
    main()