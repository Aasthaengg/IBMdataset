N = int(input())

print(0)
MorF = input()
if MorF == 'Vacant':
    exit()

iSt = 1
iEn = N - 1
seat = MorF
while True:
    iMid = (iSt + iEn) // 2

    print(iMid)
    MorF = input()
    if MorF == 'Vacant':
        break

    if MorF == seat:
        if (iMid - iSt) % 2:
            iSt = iMid + 1
            seat = MorF
        else:
            iEn = iMid - 1
    else:
        if (iMid - iSt) % 2:
            iEn = iMid - 1
        else:
            iSt = iMid + 1
            seat = MorF
