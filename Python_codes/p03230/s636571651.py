def 解():
    iN = int(input())

    #これも解法を見て作った

    iK = int((2 * iN) ** 0.5)
    if 2 * iN != iK * (iK +1 ) :
        print("No")
    else:
        print("Yes")
        print(iK+1)
        aD = [ [0] * iK for _ in range(iK)]
        iMaxCol = 0
        iRow = 0
        iCol = 0
        for i in range(1,iN+1):
            aD[iRow][iCol] = i
            if iCol == iMaxCol:
                iMaxCol += 1
                iRow += 1
                iCol = 0
            else:
                iCol += 1

        oAns = []
        iRC = 0
        iStartCol = 0
        iStartRow = 0
        for i in range(iK):
            aTmp = []
            aTmp.append(iK)
            for j in range(iK):
                if iRC == 0:
                    aTmp.append(aD[iStartRow][j])
                else:
                    aTmp.append(aD[j][iStartCol])
                if j == iStartCol:
                    iRC = 1
            oAns.append(" ".join([str(_) for _ in aTmp]))
            iStartCol += 1
            iStartRow += 1
            iRC = 0
        aTmp = []
        aTmp.append(iK)
        for i in range(iK):
            aTmp.append(aD[i][i])

        oAns.append(" ".join([str(_) for _ in aTmp]))
        print("\n".join(oAns))
解()
