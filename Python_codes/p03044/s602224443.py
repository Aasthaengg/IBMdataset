import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a,b,c = map(int,input().split())
        a -= 1
        b -= 1
        G[a].append((b,c))
        G[b].append((a,c))
    
    color = [0] * N
    dist = [-1] * N
    stack = [0]
    dist[0] = 0
    while stack:
        v = stack.pop()
        for e,c in G[v]:
            if dist[e] >= 0:
                continue
            dist[e] = dist[v] + c
            color[e] = dist[e]%2
            stack.append(e)
    print('\n'.join(map(str,color)))
if __name__ == '__main__':
    main()