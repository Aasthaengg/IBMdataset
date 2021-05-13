import sys
sys.setrecursionlimit(10000000)


def main():
    n = int(input())
    
    G=[[] for _ in range(n)]
    for _ in range(n-1):
        u,v,w = map(int, input().split())
        G[u-1].append([v-1,w])
        G[v-1].append([u-1,w])
    ans=[-1]*n
    
    def sub(node,distance):
        for next_node, edge in G[node]:
            if ans[next_node]==-1:
                ans[next_node]=(distance+edge)%2
                sub(next_node,(distance+edge)%2)
    sub(0,0)
    
    for i in ans:
        print(i)
main()