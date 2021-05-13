def Cfun():
    lines = int(input())
    inputLst = []
    for i in range(lines):
        inputLst.append(input())
    itemSets = set(inputLst)
    print(len(itemSets))


Cfun()