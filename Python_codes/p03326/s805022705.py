n, m = map(int, input().split())
list_XYZ = [ list(map(int,input().split(" "))) for i in range(n)]
list_ANS = [[] for _ in range(8)]

for i in range(n):
    l = list_ANS[0]
    l.append(list_XYZ[i][0]+list_XYZ[i][1]+list_XYZ[i][2])

for i in range(n):
    l = list_ANS[1]
    l.append(-list_XYZ[i][0]+list_XYZ[i][1]+list_XYZ[i][2])

for i in range(n):
    l = list_ANS[2]
    l.append(list_XYZ[i][0]-list_XYZ[i][1]+list_XYZ[i][2])

for i in range(n):
    l = list_ANS[3]
    l.append(list_XYZ[i][0]+list_XYZ[i][1]-list_XYZ[i][2])

for i in range(n):
    l = list_ANS[4]
    l.append(list_XYZ[i][0]-list_XYZ[i][1]-list_XYZ[i][2])

for i in range(n):
    l = list_ANS[5]
    l.append(-list_XYZ[i][0]+list_XYZ[i][1]-list_XYZ[i][2])

for i in range(n):
    l = list_ANS[6]
    l.append(-list_XYZ[i][0]-list_XYZ[i][1]+list_XYZ[i][2])

for i in range(n):
    l = list_ANS[7]
    l.append(-list_XYZ[i][0]-list_XYZ[i][1]-list_XYZ[i][2])

ans = 0

for i in range(8):
    l = list_ANS[i]
    l.sort()
    ans = max(ans, abs(sum(l[:m])), abs(sum(l[-m:])))

if m == 0:
    ans = 0
print(ans)