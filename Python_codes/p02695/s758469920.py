n, m, q = map(int, input().split())

a = [0] * q
b = [0] * q
c = [0] * q
d = [0] * q

for i in range(q):
    a[i], b[i], c[i], d[i] = map(int, input().split())
    a[i], b[i] = a[i] - 1, b[i] - 1

ans = 0

def calc(x):
    global ans
    score = 0
    for i in range(q):
        if x[b[i]] - x[a[i]] == c[i]:
            score += d[i]
    ans = max(ans, score)

def dfs(x):
    if len(x) == n:
        calc(x)
        return

    for i in range(x[-1], m+1):
        x.append(i)
        dfs(x)
        x.pop()

dfs([1])
print(ans)
