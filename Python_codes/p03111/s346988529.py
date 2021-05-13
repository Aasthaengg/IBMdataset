def f(x):
    if len(x) == n:
        p.append(x)
    else:
        for i in S:
            f(x+[i])

n , a , b , c = map(int,input().split())
take = [int(input()) for i in range(n)]
S = [0,1,2,3]
p = []
f([])
ans = 10**9
for i in range(len(p)):
    sai = [0,0,0]
    cou = 0
    for j in range(n):
        if p[i][j] != 3:
            if sai[p[i][j]] == 0:
                cou -= 10
            sai[p[i][j]] += take[j]
            cou += 10
    sai.sort()
    if sai[0] == 0:
        continue
    cou += abs(sai[0]-c)+abs(sai[1]-b)+abs(sai[2]-a)
    ans = min(ans,cou)
    
print(ans)