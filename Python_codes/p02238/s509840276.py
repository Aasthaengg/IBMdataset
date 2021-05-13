import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

global time
time = 0

def dfs(u: int, visited: list, d: list, f: list, M: list, n: int):
    global time
    visited[u] = True
    time += 1
    d[u] = time
    for j in range(n):
        if M[u][j] == 1 and not visited[j]:
            dfs(j, visited, d, f, M, n)
    time += 1
    f[u] += time

def main():
    n = int(input())
    visited = [False] * n
    M = [[0]*n for _ in range(n)]
    for _ in range(n):
        a = list(map(int, input().split()))
        for i in range(a[1]):
            M[a[0]-1][a[i+2]-1] = 1
    d = [0] * n
    f = [0] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, d, f, M, n)
    for i in range(n):
        print(i+1, d[i], f[i])

if __name__ == '__main__': main()
