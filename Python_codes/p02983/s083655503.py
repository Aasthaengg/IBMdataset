L,R = (int(x) for x in input().split())
ModL = list(x%2019 for x in range(L,min(L+2019,R+1)))
if 0 in ModL:
    print('0')
else:
    MIN = 2019
    for I in range(0,len(ModL)-1):
        for II in range(I+1,len(ModL)):
            if (ModL[I]*ModL[II])%2019<MIN:
                MIN = (ModL[I]*ModL[II])%2019
    print(MIN)