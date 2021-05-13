n, c, k, *T = map(int, open(0).read().split())
T.sort()
ans = s = 0
while s < n:
    t = T[s] + k
    X = [T[s]]
    for i in range(s+1, min(n, s+c)):
        if T[i] <= t:
            X.append(T[i])
        else:
            break
    s += len(X)
    ans += 1
print(ans)