import itertools

def allCombination(n):
    switch = [i for i in range(1,n+1)] 
    slis = []
    for i in range(0,n+1):
        for pair in itertools.combinations(switch, i):
            slis.append(pair)
    return slis

n,m = map(int,input().split())
kS = [list(map(int,input().split())) for i in range(m)]
p = list(map(int,input().split()))

slis = allCombination(n)

cnt = 0
for s in slis:
    flag = 1
    for i,eachs in enumerate(kS):
        same = set(eachs[1:]) & set(s)
        if len(same) % 2 != p[i]:
            flag = 0
    
    if flag:
        cnt += 1

print(cnt)