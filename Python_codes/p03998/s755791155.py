SA = list(input())
SB = list(input())
SC = list(input())

tmp = SA[0]
SA.remove(tmp)
for i in range(1000):
    if tmp == 'a':
        try:
            tmp = SA[0]
            SA.remove(SA[0])
        except:
            print('A')
            break
    elif tmp == 'b':
        try:
            tmp = SB[0]
            SB.remove(SB[0])
        except:
            print('B')
            break
    else:
        try:
            tmp = SC[0]
            SC.remove(SC[0])
        except:
            print('C')
            break