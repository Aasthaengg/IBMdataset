XYZ = list(map(int, input().split()))
tmp = XYZ[0]
XYZ[0] = XYZ[1]
XYZ[1] = tmp
tmp = XYZ[0]
XYZ[0] = XYZ[2]
XYZ[2] = tmp
print(" ".join(str(n) for n in XYZ))