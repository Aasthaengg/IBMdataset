import math

x1,y1,x2,y2 = raw_input().split()

tei  = float(x2) - float(x1)
taka = float(y2) - float(y1)

if tei == taka:
    st = math.sqrt(2)
    answ = st * tei
    print answ
if tei != taka:
    answ = (tei*tei) + (taka*taka)
    print math.sqrt(answ)