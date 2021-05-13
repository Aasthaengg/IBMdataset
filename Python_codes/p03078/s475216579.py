x, y, z, K = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
Z = list(map(int, input().split()))
XY = []
for i in range(x):
    for j in range(y):
        XY.append(X[i]+Y[j])
XY.sort()
Z.sort()
XYZ = []
for x in XY[::-1][:K]:
    for z in Z:
        XYZ.append(x+z)
XYZ.sort()
print(*XYZ[::-1][:K])
