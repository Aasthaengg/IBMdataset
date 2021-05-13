from __future__ import print_function
n = int(raw_input())
bilding1 = [[" 0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0"],
           [" 0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0"],
           [" 0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0"]
           ]
bilding2 = [[" 0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0"],#35~44
           [" 0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0"],#46~55
           [" 0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0"]
           ]
bilding3 = [[" 0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0"],#69~78
           [" 0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0"],#80~89
           [" 0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0"]
           ]
bilding4 = [[" 0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0"],#103~112
           [" 0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0"],#114~123
           [" 0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0 ","0"]
           ]
bilding = []
bilding.append(bilding1)
bilding.append(bilding2)
bilding.append(bilding3)
bilding.append(bilding4)

for i in range(0,n):
    inf = raw_input()
    inf= inf.split(" ")
    b = int(inf[0]) -1
    f = int(inf[1]) -1
    r = int(inf[2]) -1
    v = int(inf[3])
    bilding[b][f][r] = int(bilding[b][f][r]) + v
    if(r == 0):
        bilding[b][f][r] = " " + str(bilding[b][f][r]) + " "
    elif(r < 9):
        bilding[b][f][r] = str(bilding[b][f][r]) + " "
    else:
        bilding[b][f][r] = str(bilding[b][f][r])

count = 0
for j in range(0,4):
    for k in range(0,3):
        for l in range(0,10):
            print((bilding[j][k][l]),end="")
        print("")
    if(count < 3):
        print("####################")
        count += 1

