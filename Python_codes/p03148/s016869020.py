n, k = map(int, input().split())
sushi = [list(map(int, input().split())) for _ in range(n)]
sushi.sort(key=lambda x: x[1], reverse=True)

leaders = []
others = []

appeared = [False] * (n + 1)
for t, d in sushi:
    if appeared[t]:
        others.append(d)
    else:
        leaders.append(d)
        appeared[t] = True

def cumsum(a):
    res = [0] * (len(a) + 1)
    for i in range(len(a)):
        res[i + 1] = res[i] + a[i]
    return res

cumsum_leaders = cumsum(leaders)
cumsum_others = cumsum(others)

ans = 0
for i in range(min(k, len(leaders)), 0, -1):
    if k - i > len(others):
        break
    score = i ** 2 + cumsum_leaders[i] + cumsum_others[k - i]
    ans = max(ans, score)

print(ans)