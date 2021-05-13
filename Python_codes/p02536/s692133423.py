import sys
sys.setrecursionlimit(2 * (10 ** 6))

def main():
    N, M = map(int, input().split())
    AB = [[] for _ in range(N)]

    for _ in range(M):
        a,b = map(lambda x: int(x)-1, input().split())
        AB[a].append(b)
        AB[b].append(a)

    def dfs(v):
        visited[v] = 1
        for i in AB[v]:
            if visited[i]:
                continue
            dfs(i)

    visited = [0]*N
    cnt = 0
    for i in range(N):
        if visited[i]:
            continue
        dfs(i)
        cnt += 1
    print(cnt-1)

if __name__ == "__main__":
    main()
