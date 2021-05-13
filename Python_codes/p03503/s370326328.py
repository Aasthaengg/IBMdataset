n = int(input())
opn = [list(map(str,input().split())) for i in range(n)]
pnt = [list(map(int,input().split())) for i in range(n)]
ma = -10**100

for i in range(1,1024):
    stt = str(format(i,'010b'))
    p = 0
    for i,sh in enumerate(opn):
        ci = 0
        for j, st in enumerate(sh):
            if stt[j] == "1" and st == "1":
                ci += 1
        p += pnt[i][ci]
    if ma < p:
        ma = p

print(ma)
