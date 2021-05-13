X,Y = map(int, input().split())

trd = 100000
srd = 200000
onrd = 300000

if X == 3 and 3 < Y:
    print(trd)
elif X == 2 and 3 < Y:
    print(srd)
elif X == 1 and 3 < Y:
    print(onrd)
elif Y == 3 and 3 < X:
    print(trd)
elif Y == 2 and 3 < X:
    print(srd)  
elif Y == 1 and 3 < X:
    print(onrd)
elif X == 3 and Y == 3:
    print((trd)+(trd))
elif X == 3 and Y == 2:
    print((trd) +(srd))
elif X == 3 and Y == 1:
    print((trd)+(onrd))
elif X == 2 and Y == 3:
    print((srd)+(trd))
elif X == 2 and Y == 2:
    print((srd)+(srd))
elif X == 2 and Y == 1:
    print((srd)+(onrd))
elif X == 1 and Y == 3:
    print((onrd)+(trd))
elif X == 1 and Y == 2:
    print((onrd) + (srd))
elif X == 1 and Y == 1:
    print((onrd)+(onrd) + 400000)
else:
    print(0)