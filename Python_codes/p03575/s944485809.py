n,m = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(m)]
ans = 0
# print(ab)
for i in range(m):
    temp = [[] for i in range(n+1)]
    v = [0]*(n+1)
    for j in range(m):
        if j==i:
            continue
        else:
            temp[ab[j][0]] += [ab[j][1]]
            temp[ab[j][1]] += [ab[j][0]]
    q = [1]
    # print(temp)
    while q:
        a = q.pop()
        for j in temp[a]:
            if v[j] == 0:
                v[j] = 1
                q.append(j)
    if v.count(1) != n:
        ans += 1
    # print(v)
print(ans)