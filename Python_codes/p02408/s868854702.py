# cording: utf-8

num = int(input())

list = []
scard = []
hcard = []
ccard = []
dcard = []

for i in range(num):
    card = input().rstrip().split(" ")
    list.append(card)

for i in range(num):
    if (list[i][0] == 'S'):
        scard.append(list[i][1])
    elif (list[i][0] == 'H'):
        hcard.append(list[i][1])
    elif (list[i][0] == 'C'):
        ccard.append(list[i][1])        
    else:
        dcard.append(list[i][1])

sscard = sorted([ int(x) for x in scard])
shcard = sorted([ int(x) for x in hcard])
sccard = sorted([ int(x) for x in ccard])
sdcard = sorted([ int(x) for x in dcard])

for i in range(1,14):
    if i not in sscard:
        print("S" + " " + str(i))
for i in range(1,14):
    if i not in shcard:
        print("H" + " " + str(i))
for i in range(1,14):
    if i not in sccard:
        print("C" + " " + str(i))
for i in range(1,14):
    if i not in sdcard:
        print("D" + " " + str(i))