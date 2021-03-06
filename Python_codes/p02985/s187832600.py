#!/usr/bin/env python3

MOD = 10 ** 9 + 7

def main():
    n, k = map(int, input().split())
    adj = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)

    res = k
    stack = [0]
    visited = [False for i in range(n)]
    while stack:
        i = stack.pop()
        visited[i] = True
        children = [x for x in adj[i] if not visited[x]]
        res *= perm((k - 1 if i == 0 else k - 2), len(children))
        res %= MOD
        for c in children:
            stack.append(c)
    print(res)

def perm(t, s):
    res = 1
    for i in range(s):
        res *= t
        res %= MOD
        t -= 1
    return res

if __name__ == "__main__":
    main()
