import sys

l = []
for i in sys.stdin:
    l.append(i.split())

for i in range(0,len(l)-1):
    if int(l[i][0]) == -1 or int(l[i][1]) == -1:
        print('F')
    elif int(l[i][0]) + int(l[i][1]) >= 80:
        print('A')
    elif int(l[i][0]) + int(l[i][1]) < 80 and int(l[i][0]) + int(l[i][1]) >= 65:
        print('B')
    elif (int(l[i][0]) + int(l[i][1]) < 65 and int(l[i][0]) + int(l[i][1]) >= 50) or int(l[i][2]) >= 50:
        print('C')
    elif int(l[i][0]) + int(l[i][1]) < 50 and int(l[i][0]) + int(l[i][1]) >= 30:
        print('D')
    else:
        print('F')
