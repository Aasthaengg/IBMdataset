H,W,D=map(int,input().split())
A = [[0]*(W+1)]
A += [[0] + list(map(int,input().split())) for _ in range(H)]
# n2idx = [None]*(H*W + 1)
routes = [[] for _ in range(D)]
for h in range(1, H+1):
    for w in range(1, W+1):
        # n2idx[A[h][w]] = (h, w)
        routes[A[h][w]%D].append((A[h][w], h, w))
        #(num, x-idx, y-idx)

Q = int(input())
costs = [[0] for _ in range(D)]
for d in range(D):
    routes[d].sort()
    # now = routes[d][0]
    for i in range(1, len(routes[d])):
        v1, h1, w1 = routes[d][i-1]
        v2, h2, w2 = routes[d][i]
        costs[d].append(costs[d][i-1] + abs(h1-h2)+abs(w1-w2))

for _ in range(Q):
    L, R = map(int, input().split())
    amari = L%D
    start = L//D
    end = R//D
    if amari == 0:
        start -= 1
        end -= 1
    print(costs[amari][end] - costs[amari][start])