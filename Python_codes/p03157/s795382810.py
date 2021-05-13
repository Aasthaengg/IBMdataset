import networkx as nx

H, W = map(int, input().split())
S = [input() for _ in range(H)]

G = nx.Graph()
G.add_nodes_from([(h, w) for h in range(H) for w in range(W)])
for h in range(H - 1):
    for w in range(W):
        if S[h][w] != S[h + 1][w]:
            G.add_edge((h, w), (h + 1, w))
for h in range(H):
    for w in range(W - 1):
        if S[h][w] != S[h][w + 1]:
            G.add_edge((h, w), (h, w + 1))

ans = 0
for component in nx.connected_components(G):
    black, white = 0, 0
    for h, w in component:
        if S[h][w] == '#':
            black += 1
        else:
            white += 1
    ans += black * white
print(ans)
