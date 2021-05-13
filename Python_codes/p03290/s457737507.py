D, G = list(map(int, input().split()))
p, c = [0,], [0,]
for _ in range(D):
    pi, ci = list(map(int, input().split()))
    p.append(pi)
    c.append(ci)
ans = 1010
for i in range(2 ** D):
    score = 0
    solve = [False] * D
    for j in range(D):
        if i >> j & 1:
            solve[j] = True
        else:
            continue
    score = sum([100 * (j + 1) * p[j + 1] + c[j + 1] for j in range(D) if solve[j]])
    num = sum([p[j + 1] for j in range(D) if solve[j]])
    maxp = len(list(filter(lambda x: not x, solve)))
    if maxp != 0:
        for i in range(1, p[maxp]):
            if score >= G:
                break
            score += 100 * maxp
            num += 1
    if score < G:
        num = 1010
    ans = min(num, ans)
print(ans)