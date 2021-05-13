A,B,M=map(int, input().split())
AList=list(map(int, input().split()))
BList=list(map(int, input().split()))
XYCList = [list(map(int, input().split())) for i in range(M)]
ANS=[min(AList)+min(BList)]
i=0
while i<M:
    ANS.append(AList[XYCList[i][0]-1]+BList[XYCList[i][1]-1]-XYCList[i][2])
    i+=1
print(min(ANS))