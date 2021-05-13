N,C = map(int,input().split())
imos = [[0]*100005 for i in range(30)]
for i in range(N):
    s,t,c = map(int,input().split())
    s -= 1
    c -= 1
    imos[c][s] += 1
    imos[c][t] -= 1
for c in range(C):
    for i in range(1,100005):
        imos[c][i] += imos[c][i-1]
for c in range(C):
    for i in range(1, 100005):
        if imos[c][i]:
            imos[c][i] = 1

ans = 0
for i in range(100005):
    cnt = 0
    for c in range(C):
        cnt += imos[c][i]
    ans = max(ans,cnt)
print(ans)