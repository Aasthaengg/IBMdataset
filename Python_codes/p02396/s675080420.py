inArray = []
while True:
    inVal = int(input())
    if inVal == 0:
        break
    inArray.append(inVal)

count = 1
for n in inArray:
    print("Case " + str(count) + ": " + str(n))
    count = count + 1
