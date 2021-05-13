import sys
input = sys.stdin.readline
from itertools import product
INF = 10**9
MOD = 10**9 + 7

def main():
    n,c = map(int,input().split())
    D = [list(map(int,input().split())) for _ in range(c)]
    grid0 = []
    grid1 = []
    grid2 = []
    for i in range(n):
        g = [int(i)-1 for i in input().split()]
        for j in range(n):
            if  (i+j)%3 == 0:
                grid0.append(g[j])
            elif (i+j)%3 == 1:
                grid1.append(g[j])
            else:
                grid2.append(g[j])
        
    
    def drew(grid):
        ans = [[INF,-2] for _ in range(3)] 
        for i in range(c):
            t = 0
            for g in grid:
                t += D[g][i]
            if t < ans[0][0]:
                ans[2] = ans[1]
                ans[1] = ans[0]
                ans[0] = [t,i]
            elif t < ans[1][0]:
                ans[2] = ans[1]
                ans[1] = [t,i]
            elif t < ans[2][0]:
                ans[2] = [t,i]

        return ans
    
    a = drew(grid0)
    b = drew(grid1)
    c = drew(grid2)
    ans = INF 
    for x,y,z in product(a,b,c):
        if  x[1] != y[1] and y[1] != z[1] and z[1] != x[1]:
            ans = min(ans,x[0]+y[0]+z[0])
    
    print(ans)
   
if __name__=='__main__':
    main()
