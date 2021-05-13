MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

ans = 1
def dfs(i,x,y,z,a,n):
    global ans
    if i == n:
        return
    if x == y == z == a[i]:
        ans *= 3
        ans %= MOD
        dfs(i + 1,x + 1,y,z,a,n)
    elif x == y == a[i]:
        ans *= 2
        ans %= MOD
        dfs(i + 1,x + 1,y,z,a,n)
    elif y == z == a[i]:
        ans *= 2
        ans %= MOD
        dfs(i + 1,x,y + 1,z,a,n)
    elif x == a[i]:
        dfs(i + 1,x + 1,y,z,a,n)
    elif y == a[i]:
        dfs(i + 1,x,y + 1,z,a,n)
    elif z == a[i]:
        dfs(i + 1,x,y,z + 1,a,n)
    else:
        ans = 0
        return

def main():
    n = int(input())
    a = list(map(int,input().split()))

    dfs(0,0,0,0,a,n)
    print(ans)

if __name__ =='__main__':
    main()   
