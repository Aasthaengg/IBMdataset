from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    H, W = map(int, input().split())
    ls = deque([])
    D = [[0] * (W+2)]
    D += ([[0] + [float("inf")]*W + [0] for i in range(H)])
    D.append([0]*(W+2))
    G = [["#"]*(W+2)]
    for i in range(H):
        line = [i for i in input().strip()]
        for j in range(W):
            if line[j] == "#":
                ls.append([i+1, j+1, 0])
                D[i+1][j+1] = 0
        G.append(["#"]+line+["#"])
    G.append([["#"]*(W+2)])

    while len(ls) > 0:
        h, w, depth = ls.popleft()
        if depth + 1 < D[h+1][w] and G[h+1][w] != "#":
            ls.append([h+1, w, depth+1])
            D[h+1][w] = depth + 1
        if depth + 1 < D[h-1][w] and G[h-1][w] != "#":
            ls.append([h-1, w, depth+1])
            D[h-1][w] = depth + 1
        if depth + 1 < D[h][w+1] and G[h][w+1] != "#":
            ls.append([h, w+1, depth+1])
            D[h][w+1] = depth + 1
        if depth + 1 < D[h][w-1] and G[h][w-1] != "#":
            ls.append([h, w-1, depth+1])
            D[h][w-1] = depth + 1

    ans = 0
    for h in range(H+2):
        ans = max(ans, max(D[h]))
        
    return ans
    
print(bfs())