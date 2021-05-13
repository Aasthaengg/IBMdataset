def 解():
    iN = int(input())

    #解法pdfを見て作ったその2

    iK = int((2 * iN) ** 0.5)
    if 2 * iN != iK * (iK +1 ) :
        print("No")
    else:
        print("Yes")
        print(iK+1)
        oAns = []
        iStart = 1
        for i in range(iK):
            oRes = [iK]
            oRes.extend(list(range(iStart,iStart+i+1)))
            iLast = oRes[-1]
            for k in range(i+1,iK):
                iLast += k
                oRes.append(iLast)
            oAns.append(" ".join([str(_) for _ in oRes]))
            iStart += i +1
        oRes = [iK]
        iStart = 0
        for i in range(0,iK):
            iStart += i +1
            oRes.append(iStart)
        oAns.append(" ".join([str(_) for _ in oRes]))
        print("\n".join(oAns))
解()
