import sys
INF = 10 ** 9
MOD = 10 ** 9 + 7
from collections import deque
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    G = [0] * (n - 1)
    for _ in range(m):
        a,b = map(int,input().split())
        if a > b:
            a,b = b,a
        a -= 1
        b -= 1
        G[a] += 1
        if b != n - 1:
            G[b] -= 1
    
    ans = 'YES'
    if G[0]%2 == 1:
        print('NO')
        return

    for i in range(1,n - 1):
        G[i] += G[i - 1]
        if G[i]%2 == 1:
            ans = 'NO'
            break
    print(ans)
if __name__=='__main__':
    main()