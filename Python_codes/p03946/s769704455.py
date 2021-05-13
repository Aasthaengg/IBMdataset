n, t = map(int, input().split())
A = tuple(map(int, input().split()))
AI = [(i, a) for i, a in enumerate(A)]
AI = sorted(AI, key=lambda x: x[1])

# 小さい順に見ていく
count = 0
maxdiff = 0
visited = [0] * n
for i, a in AI:
    if visited[i]:
        continue
    visited[i] = 1

    for j in range(i+1, n):
        if visited[j]:
            break
        visited[j] = 1
        diff = A[j] - a
        if diff > maxdiff:
            count = 1
            maxdiff = diff
        elif diff == maxdiff:
            count += 1
print(count)
