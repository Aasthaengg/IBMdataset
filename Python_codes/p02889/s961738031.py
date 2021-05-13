import sys
input = sys.stdin.readline

def main():
    n, m, l = map(int, input().split())
    dist = [[float('inf')]*n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        dist[a][b] = c
        dist[b][a] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    dist2 = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= l:
                dist2[i][j] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist2[i][j] = min(dist2[i][j], dist2[i][k] + dist2[k][j])


    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        if dist2[s][t] == float('inf'):
            print(-1)
            continue
        ans = dist2[s][t]
        print(ans-1)

if __name__ == "__main__":
    main()