XY = input().split()
X = int(XY[0])
Y = int(XY[1])
l = []
for i in range(X+1):
    for j in range (X+1):
        if i + j == X:
            if (4*i + 2*j) == Y:
                l.append("Yes")
            else:
                l.append("No")
if l.count("Yes") > 0:
    print("Yes")
else:
    print("No")
        #print(str(i) + "," + str(j))