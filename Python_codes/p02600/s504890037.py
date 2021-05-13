x= int(input())
cont=0
if x>= 400 and x<=599:
    cont=8
elif x>= 600 and x<=799:
    cont=7
elif x>= 800 and x<=999:
    cont=6
elif x>= 1000 and x<=1199:
    cont=5
elif x>= 1200 and x<=1399:
    cont=4
elif x>= 1400 and x<=1599:
    cont=3
elif x>= 1600 and x<=1799:
    cont=2
elif x>= 1800 and x<=1999:
    cont=1
print(cont)