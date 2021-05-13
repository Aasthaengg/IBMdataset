X = []
def dfs(k, L):
    global cnt
    if k:
        X.append(int("".join(map(str, L))))
    if k == K:
        return
    if k == 0:
        for i in range(1, 10):
            dfs(k + 1, L + [i])
    else:
        l = L[-1]
        for i in range(max(l-1, 0), min(l+2, 10)):
            dfs(k + 1, L + [i])

K = 10
dfs(0, [])
print(sorted(X)[int(input()) - 1])