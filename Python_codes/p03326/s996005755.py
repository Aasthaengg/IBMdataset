from itertools import product

N, M = map(int, input().split())
X = []
for i in range(N):
    x, y, z = map(int, input().split())
    X.append([x, y, z])

l = (-1, 1)

ans = 0
for i, j, k in product(*([l]*3)):
    xs = [x*i+y*j+z*k for x, y, z in X]
    xs.sort(reverse=True)
    ans = max(ans, sum(xs[:M]))
print(ans)