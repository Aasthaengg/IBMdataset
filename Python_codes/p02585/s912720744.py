n , k = map(int,input().split())
p = list(map(int,input().split()))
c = list(map(int,input().split()))
loop = []
visit = [(-1,-1) for i in range(n)]
cou = -1
for i in range(n):
    if visit[i] != (-1,-1):
        continue
    cou += 1
    tyu  = [i]
    now = i
    visit[i] = (cou,0)
    t = 1
    while True:
        nex = p[now] - 1
        if nex == i:
            break
        visit[nex] = (cou,t)
        tyu.append(nex)
        now = nex
        t += 1
    loop.append(tyu)

ans = []

for i in range(n):
    p = loop[visit[i][0]][visit[i][1]:] + loop[visit[i][0]][:visit[i][1]]
    kar = [0]
    kouho = []
    losum = 0
    lokz = len(p)
    for j in p:
        losum += c[j]
        kar.append(kar[-1] + c[j])
    if losum >= 0:
        for l in range(lokz+1):
            if l > k:
                break
            cou = losum*((k-l)//lokz) + kar[l]
            kouho.append(cou)
    elif losum < 0:
        for l in range(1,lokz+1):
            if l > k:
                break
            cou = kar[l]
            kouho.append(cou)
    ans.append(max(kouho))
print(max(ans))
