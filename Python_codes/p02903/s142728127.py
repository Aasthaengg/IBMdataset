H, W, A, B  = map(int, input().split())
graph = [[0]*W for _ in range(H)]
for i in range(B):
    for j in range(A, W):
        graph[i][j] = 1
for i in range(B, H):
    for j in range(A):
        graph[i][j] = 1
for line in graph:
    print("".join(map(str, line)))
