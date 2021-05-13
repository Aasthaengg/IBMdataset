import itertools

n,m = map(int,input().split())
ks = [list(map(int,input().split())) for i in range(m)]
p = list(map(int,input().split()))

#onにするスイッチを選ぶ
switch = [i for i in range(1,n+1)]
comb = []
for i in range(n+1):
    for v in itertools.combinations(switch,i):
        comb.append(v)

ans = 0
for i in comb:
    for j in range(m):
        tmp = 0
        for l in range(1,ks[j][0]+1):
            if ks[j][l] in i:
                tmp += 1
        if tmp%2 != p[j]:
            break
    else:
        ans += 1

print(ans)