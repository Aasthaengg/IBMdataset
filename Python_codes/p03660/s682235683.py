import sys
input = sys.stdin.readline
INF = 10**20
MOD = 10**9 + 7
sys.setrecursionlimit(100000000)

def main():
    n = int(input())
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    
    depth = [-1] * n
    depth[0] = 0
    snuke = [0] * n
    snuke[-1] = 1
    children = [1] * n

    def dfs(i):
        if len(G[i]) == 0:
            return
        else:
            for e in G[i]:
                if depth[e] == -1:
                    depth[e] = depth[i] + 1
                    dfs(e)
                    snuke[i] |= snuke[e]
                    children[i] += children[e] 
  
    dfs(0)
    white = depth[-1]//2 + 1
    for i in range(n):
        if depth[i] == white and snuke[i]:
            sp = children[i]
            fp = n - sp
            break
    
    if  fp > sp:
        print('Fennec')
    else:
        print('Snuke')  
if __name__=='__main__':
    main()