import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 9)

def main():
    N,M = map(int,input().split())
    
    edge = [[] for _ in range(N)]
    for _ in range(M):
        x,y = map(int,input().split())
        edge[x-1].append(y-1)
        
    dist = [-1 for _ in range(N)]
            
    def dfs(s):
        if dist[s] != -1:
            return dist[s]
        else:
            ret = 0
            for fol in edge[s]:
                ret = max(ret,dfs(fol)+1)
            dist[s] = ret
            return ret

    for i in range(N):
        dfs(i)
        
    print(max(dist))
    
if __name__ == "__main__":
    main()
