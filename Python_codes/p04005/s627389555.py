# https://atcoder.jp/contests/agc004/tasks/agc004_a

a, b, c = map(int, input().split())

edges = [a, b, c]
edges.sort()

ans = edges[0] * edges[1] * (edges[2] % 2)
print(ans)