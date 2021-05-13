numListA = []
numListB = []

x = -1
y = -1
num = 0

while x != 0 or y != 0: 
    if x == -1:
        x, y = (int(a) for a in input().split())

    else:
        numListA = numListA + [x]
        numListB = numListB + [y]
        x, y = (int(a) for a in input().split())
        num += 1

for i in range(num):
    if(numListA[i] > numListB[i]):
        print("%d %d" % (numListB[i], numListA[i]))
    else:
        print("%d %d" % (numListA[i], numListB[i]))

