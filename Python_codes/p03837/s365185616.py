import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    dist = [[float('inf') for i in range(N)] for j in range(N)]
    
    r = [[-1 for i in range(N)] for j in range(N)]
    
    for i in range(N): dist[i][i] = 0
    for i in range(M):
        a, b, c = map(int, input().split())
        a -= 1; b -= 1
        dist[a][b] = c
        dist[b][a] = c
        
        r[a][b] = i
        r[b][a] = i
        
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k]+dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]
                    r[i][j] = r[k][j]
        
    ans = set()    
    for a in r: ans.update(set(a))    
    print(M-len(ans)+1)

if __name__ == '__main__':
    main()