n,m = map(int,input().split())
pS = [list(input().split()) for i in range(m)]

for _ in range(m) :
    pS[_][0] = int(pS[_][0])

ac = [0]*n
wa = [0]*n

for i in range(m) :
    if pS[i][1] == "AC" :
        if ac[pS[i][0]-1] == 0 :
            ac[pS[i][0]-1] += 1
    elif pS[i][1] == "WA" :
        if ac[pS[i][0]-1] == 0 :
            wa[pS[i][0] - 1] += 1

awa=0
for i in range(n) :
    if ac[i] == 1 :
        awa += wa[i]

print(sum(ac),awa)
