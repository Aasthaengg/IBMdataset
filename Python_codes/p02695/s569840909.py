import itertools

n, m, q = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(q)]


ans = 0
for iter in itertools.combinations_with_replacement(range(1, m+1), n):
    score = 0
    for i in range(q):
        a, b, c, d = L[i]
        if iter[b-1]-iter[a-1]==c:
            score += d

    ans = max(ans, score)

print(ans)