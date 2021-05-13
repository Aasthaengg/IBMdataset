import sys
sys.setrecursionlimit(10 ** 7)

def solve(g, p, index, y, z, k):
    p[index] = k - y - z
    x = 1
    for i in g[index]:
        if p[i] == -1:
            solve(g, p, i, x, y, k)
            y += 1

def main():
    n, k = map(int, input().split())
    graph =[[] for _ in range(n)]
    p = [-1]*n
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    s = None
    for i in range(n):
        if len(graph[i]) == 1:
            s = i
            break
    if s is None:
        print(k)
        sys.exit()
    solve(graph, p, s, 0, 0, k)
    ans = 1
    for i in p:
        ans *= i
        ans %= 10**9 + 7
    print(ans)

if __name__ == "__main__":
    main()