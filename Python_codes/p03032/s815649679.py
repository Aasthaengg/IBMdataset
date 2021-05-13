n, k = map(int, input().split())
v = list(map(int, input().split()))
m = min(n, k)
max_score = 0
for i in range(m+1):
    for j in range(m+1-i):
        vals = v[:i] if j == 0 else v[:i] + v[-j:]
        minus = list(filter(lambda x : x < 0, vals))
        minus.sort()
        score = sum(vals) - sum(minus[:min(k - i - j, len(minus))])
        if max_score < score:
            max_score = score
print(max_score)