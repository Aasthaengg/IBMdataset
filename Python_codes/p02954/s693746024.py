s = input()
RLSegment = [] # tuple (number of R, number of L)
isRNow = True
isLNow = False
rCount = 0
lCount = 0
for elem in s:
    if isRNow and elem == "R":
        rCount += 1
    elif isRNow and elem == "L":
        isRNow = False
        isLNow = True
        lCount = 1
    elif isLNow and elem == "L":
        lCount += 1
    else:
        RLSegment.append((rCount,lCount))
        isRNow = True
        isLNow = False 
        rCount = 1
        lCount = 0
RLSegment.append((rCount,lCount))

indexAns = 0
ans = []
for elem in RLSegment:
    endRCount = elem[0] // 2 + elem[0] % 2 + elem[1] // 2
    endLCount = elem[0] // 2 + elem[1] // 2 + elem[1] % 2
    for i in range(indexAns,indexAns + elem[0] - 1):
        ans.append('0')
    ans.append(str(endRCount))
    ans.append(str(endLCount))
    for i in range(indexAns + elem[0] + 1,indexAns + elem[0] + elem[1]):
        ans.append('0')
    indexAns += elem[0] + elem[1]
print(' '.join(ans))