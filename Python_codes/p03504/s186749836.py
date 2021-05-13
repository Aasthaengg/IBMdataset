n,C = map(int,input().split())
ch = [[0]*(200001) for _ in range(C)]
m = 0
for _ in range(n):
    s,t,c = map(int,input().split())
    s = s*2-1
    t *= 2
    c -= 1
    ch[c][s] += 1
    ch[c][t] -= 1
    m = max(m,t)

cnt = [0]*(m+1)
for c in range(C):
    for i in range(1,m+1):
        ch[c][i] += ch[c][i-1]
        if ch[c][i-1] == 0 and ch[c][i] > 0: cnt[i] += 1
        if ch[c][i-1] > 0 and ch[c][i] == 0: cnt[i] -= 1

for i in range(1,m+1): cnt[i] += cnt[i-1]
print(max(cnt))