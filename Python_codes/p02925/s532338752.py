n = int(input())

#big+small*1000から出る辺の先
edge = [[] for _ in range(2*(10**6))]
#used -1:点なし else:入力本数
used = [-1]*(2*(10**6))

for i in range(1,n+1):
    a = tuple(map(int,input().split()))
    fr = None
    for e in a:
        go = max(i,e) + min(i,e)*1000

        if fr != None:
            if used[fr] < 0:
                used[fr] = 0
            if used[go] < 0:
                used[go] = 0
            edge[fr].append(go)
            used[go] += 1
        fr = go


res = 0
ctr = 0
tank = []
new = []
for i,e in enumerate(used):
    if e == 0:
        new.append(i)
        ctr += 1

while len(new) > 0:
    tank = []
    for p in new:
        for e in edge[p]:
            used[e] -= 1
            if used[e] == 0:
                tank.append(e)
                ctr += 1
    new = tank
    res += 1

if ctr < n*(n-1)//2:
    print(-1)
else:
    print(res)

