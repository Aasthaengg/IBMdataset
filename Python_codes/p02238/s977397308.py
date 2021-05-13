# coding: utf-8
# Your code here!

import sys
read = sys.stdin.read
readline = sys.stdin.readline


def dfs(G, v, d, f, time):
    time += 1
    d[v] = time

    for e in G[v]:
        if d[e] == 0:
            time = dfs(G, e, d, f, time)

    time += 1
    f[v] = time

    return time


def main():
    n = int(readline())

    E = [[]]
    for _ in range(n):
        u,k,*v = map(int, readline().split())
        E.append(v)

    d = [0] * (n+1)
    f = [0] * (n+1)
    time = 0
    
    for i in range(1,n+1):
        if d[i] == 0:
            time = dfs(E, i, d, f, time)
    
    for i in range(1, n+1):
        print(i, d[i], f[i])


if __name__ == "__main__":
    main()


