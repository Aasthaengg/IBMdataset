n = int(input())
g = [[-1 for _ in range(15)] for _ in range(15)]
for i in range(n) :
    m = int(input())
    for j in range(m) :
        x,y = map(int, input().split())
        #人iが「人xはyである」と証言している
        g[i][x-1] = y

ans = 0
for i in range(1<<n) :
    honests = [0] * n
    for j in range(n) :
        if (i>>j) & 1 :
            honests[j] = 1
    ok = True
    for j in range(n) :
        if honests[j] : #正直者の証言だけ検証する
            for k in range(n) :
                if g[j][k] == -1 :
                    continue
                if g[j][k] != honests[k] :
                    ok = False
    if ok :
        ans = max(ans, honests.count(1))

print(ans)
