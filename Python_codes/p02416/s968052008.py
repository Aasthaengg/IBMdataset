while True:
    val = input()
    if val == "0":
        break

    numList = list(map(int, list(val)))
    sum = 0
    for i in range(len(numList)):
        sum += int(numList[i])

    print(sum)
