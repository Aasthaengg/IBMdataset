def main():
    N = int(input())
    aD = []
    if N % 2 :
        aD = [[i,N-i] for i in range(1,(N+1)//2)]
        aD.append([N])
    else:
        aD = [[i,N+1-i] for i in range(1,(N//2)+1)]
    iD = len(aD)
    dRes = set()
    def strfy(aD):
        return " ".join(str(_) for _ in sorted(aD))
    for i in range(iD):
        for j in range(iD):
            if i == j :
                pass
            else:
                if len(aD[i]) == 1:
                    dRes.add(strfy([aD[i][0],aD[j][0]]))
                    dRes.add(strfy([aD[i][0],aD[j][1]]))
                elif len(aD[j])== 1:
                    dRes.add(strfy([aD[i][0],aD[j][0]]))
                    dRes.add(strfy([aD[i][1],aD[j][0]]))
                else:
                    dRes.add(strfy([aD[i][0],aD[j][0]]))
                    dRes.add(strfy([aD[i][0],aD[j][1]]))
                    dRes.add(strfy([aD[i][1],aD[j][0]]))
                    dRes.add(strfy([aD[i][1],aD[j][1]]))
    print(len(dRes))
    print(*dRes,sep="\n")
main()
