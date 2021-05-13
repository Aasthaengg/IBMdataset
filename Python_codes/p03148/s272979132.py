# 写経
N, K = map(int, input().split())


top = [0] * N
sub = []
for _ in range(N):
    t, d = map(int, input().split())
    t -= 1
    if top[t] == 0:
        top[t] = d
    else:
        if top[t] >= d:
            sub.append(d)
        else:
            sub.append(top[t])
            top[t] = d
top.sort(reverse=True)
sub.sort(reverse=True)


res = [0]
for i in range(N):
    if top[i] != 0:
        res.append(res[-1] + top[i])
    else:
        res.append(-1)
w = [0]
for i in range(len(sub)):
    w.append(w[-1] + sub[i])


ans = 0
for i in range(1, K+1):
    if (len(w) - 1 >= K-i) and (res[i] != -1):
        ans = max(res[i] + w[K-i] + i**2, ans)
print(ans)
