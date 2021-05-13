from collections import Counter
h, w = map(int, input().split())
C = [[0]*10 for _ in range(10)]
cost = []
for i in range(10):
    C[i] = list(map(int, input().split()))

for k in range(10):
    for i in range(10):
        for j in range(10):
            C[i][j] = min(C[i][j], C[i][k]+C[k][j])
costs = [C[i][1] for i in range(10)]

A = Counter()
for i in range(h):
    A += Counter(list(map(int,input().split())))

ans = 0
for key, val in A.items():
    if key!=-1:
        ans += val*costs[key]
print(ans)