numList = []

a = -1
num = 0
while a != 0:
    if a == -1:
        a = int(input())

    else:
        numList = numList + [a]
        a = int(input())
        num += 1

for i in range(num):
    print("Case %d: %d" % (i+1, numList[i]))

