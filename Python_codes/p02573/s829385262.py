N, M = map(int, input().split())
r = [-1] * (N + 1)

def root(x):
        if r[x] < 0:
                return x
        return root(r[x])

for i in range(M):
        x, y = map(int, input().split())
        x = root(x)
        y = root(y)
        if x == y:
                continue
        if r[x] > r[y]:
                x, y = y, x
        r[x] += r[y]
        r[y] = x 

print(-min(r))