N,C = map(int,input().split())
ch = {}
for _ in range(N):
    s,t,c = map(int,input().split())
    if c not in ch:
        ch[c] = [0 for _ in range(2*10**5+2)]
    for i in range(2*s-1,2*t):
        ch[c][i]=1
cmax = 0
for i in range(2*10**5+2):
    cnt = 0
    for c in ch:
        if ch[c][i]==1:
            cnt += 1
    cmax = max(cmax,cnt)
print(cmax)