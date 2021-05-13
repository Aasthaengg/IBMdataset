n,tt,m,*px = [list(map(int, s.split())) for s in open(0)]

stt = sum(tt)

for p,x in px:
    print(stt-tt[p-1]+x)