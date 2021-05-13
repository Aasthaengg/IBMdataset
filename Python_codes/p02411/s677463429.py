def ifExit(a):
    if a[0] =='-1' and a[1] =='-1' and a[2] =='-1':
        return True
    else:
        return False



l=[]

while(True):
    tmp = input().split()
    if ifExit(tmp): break

    m=int(tmp[0])
    f=int(tmp[1])
    r=int(tmp[2])

    if (m < 0) or (f < 0) :
        l.append('F')
    elif (m+f >= 80):
        l.append('A')
    elif (80 > m+f and m+f >= 65):
        l.append('B')
    elif (65 > m+f and m+f >= 50):
        l.append('C')
    elif (50 > m+f and m+f >= 30):
        if r>=50:
            l.append('C')
        else:
            l.append('D')
    else:
        l.append('F')

print('\n'.join(l))