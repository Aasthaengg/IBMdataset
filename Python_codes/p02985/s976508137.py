import sys

mod = 1000000007

n, k = map(int, input().split())
nexts = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    nexts[a].append(b)
    nexts[b].append(a)

# [score, defined]
scores = [[0, 0] for _ in range(n+1)]
result = 1
nextList = [1]
while len(nextList) > 0:
    i = nextList.pop()
    defined = 0
    for j in nexts[i]:
        if scores[j][0] != 0:
            defined += scores[j][1]
        else:
            nextList.append(j)
        scores[j][1] += 1
    if k - defined <= 0:
        result = 0
        break
    result = result * (k-defined) % mod
    scores[i][0] = k-defined
    scores[i][1] += 1

print(result)

