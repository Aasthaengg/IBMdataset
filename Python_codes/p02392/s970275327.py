inputStr = input()
numList = inputStr.split(' ')
numList = [int(x) for x in numList]
numList2 = numList.copy()
numList.sort()
numSet = set(numList)

#print('numList: ',numList)
#print('numList2: ', numList2)

if numList == numList2 and len(numList)==len(numSet):
    print('Yes')
else:
    print('No')