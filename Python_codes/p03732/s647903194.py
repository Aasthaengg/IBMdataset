N,W = map(int,input().split())
wv = {}
for i in range(N):
    w,v = map(int,input().split())
    if w not in wv.keys():
        wv[w] = []
    wv[w].append(v)

for w in wv.keys():
    wv[w] = sorted(wv[w],reverse=True)

wv_ruiseki = {}
for w in wv.keys():
    wv_ruiseki[w] = [0,wv[w][0]]
    for i in range(2,len(wv[w])+1):
        wv_ruiseki[w].append(wv_ruiseki[w][i-1] + wv[w][i-1])


w = []
for i in wv.keys():
    w.append(i)

ans = 0
if len(w) == 1:

    for i in range(len(wv[w[0]])+1):
        if w[0]*i <= W:
            ans = max(ans , wv_ruiseki[w[0]][i])
elif len(w) == 2:

    for i in range(len(wv[w[0]])+1):
        for j in range(len(wv[w[1]])+1):
            if w[0]*i + w[1]*j <= W:
                ans = max(ans , wv_ruiseki[w[0]][i]+ wv_ruiseki[w[1]][j])

elif len(w) == 3:

    for i in range(len(wv[w[0]])+1):
        for j in range(len(wv[w[1]])+1):
            for k in range(len(wv[w[2]])+1):
                if w[0]*i + w[1]*j + w[2]*k <= W:
                    ans = max(ans , wv_ruiseki[w[0]][i]+ wv_ruiseki[w[1]][j] + wv_ruiseki[w[2]][k])
elif len(w) == 4:
    for i in range(len(wv[w[0]])+1):
        for j in range(len(wv[w[1]])+1):
            for k in range(len(wv[w[2]])+1):
                for t in range(len(wv[w[3]])+1):
                    if w[0]*i + w[1]*j + w[2]*k + w[3]*t <= W:
                        ans = max(ans , wv_ruiseki[w[0]][i]+ wv_ruiseki[w[1]][j] + wv_ruiseki[w[2]][k] + wv_ruiseki[w[3]][t])


print(ans)
