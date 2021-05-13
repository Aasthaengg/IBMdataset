n, c = map(int, input().split())
XR = [list(map(int,input().split())) for i in range(n)]
XL = [[c-XR[i][0], XR[i][1]] for i in range(n)]
XL.sort()

CR = []
cal = 0
for i in range(n):
    dis = XR[i][0]
    cal += XR[i][1]
    CR.append([cal-dis, dis])


CSR = [CR[0][0]]
for i in range(n-1):
    CSR.append(max(CSR[i], CR[i+1][0]))

CL = []
cal = 0
for i in range(n):
    dis = XL[i][0]
    cal += XL[i][1]
    CL.append([cal-dis, dis])


CSL = [CL[0][0]]
for i in range(n-1):
    CSL.append(max(CSL[i], CL[i+1][0]))


# print(CSR)
# print(CSL)
# print(CR)
# print(CL)

ans = max(max(CSR), max(CSL))
for i in range(n-1):
    # print(CL[i][0]-CL[i][1]+CSR[n-2-i], CL[i][0],CL[i][1],CSR[n-2-i])
    ans = max(ans, CL[i][0]-CL[i][1]+CSR[n-2-i])
    ans = max(ans, CR[i][0]-CR[i][1]+CSL[n-2-i])

print(max(ans, 0))
