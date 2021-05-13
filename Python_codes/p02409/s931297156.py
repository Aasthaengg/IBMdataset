import sys
write=sys.stdout.write

buildings=[[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]
for i in range(0,4):
    for j in range(0,3):
        for k in range(0,10):
            buildings[i][j].append(0)

informations=int(input())

for i in range(0,informations):
    information=[]
    information=input().split()
    information[0]=int(information[0])
    information[1]=int(information[1])
    information[2]=int(information[2])
    information[3]=int(information[3])
    buildings[information[0]-1][information[1]-1][information[2]-1]+=information[3]

for i in range(0,4):
    for j in range(0,3):
        for k in range(0,10):
            write(' ')
            write(str(buildings[i][j][k]))
        print()
    if i !=3:
        for j in range(0,20):
            write('#')
        print()