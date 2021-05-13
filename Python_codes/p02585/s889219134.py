n, k = map(int, input().split())


ps = list(map(int, input().split()))
cs = list(map(int, input().split()))

graphs = []
vGraphs = []
flags = [False]*n
sumDict = dict()
for i in range(len(ps)):
    p = ps[i]
    index = p - 1
    if flags[index]:
        continue

    current = set()
    values = set()
    currentIndex = index
    while True:
        if flags[currentIndex]:
            break

        current.add(currentIndex)
        values.add(cs[currentIndex])
        flags[currentIndex] = True
        nextIndex = ps[currentIndex] - 1
        currentIndex = nextIndex
    graphs.append(current)
    vGraphs.append(values)

answer = -float('inf')
for i in range(n):

    searchI = 0
    loopSum = 0
    nextIndex = i
    loopCount = 0
    while True:
        nextIndex = ps[nextIndex] - 1
        loopSum += cs[nextIndex]
        loopCount += 1
        if nextIndex == i:
            break

    total = loopSum

    currentSum = 0
    count = 0
    ci = i
    while True:
        count += 1
        if count > k:
            break
        loop = (k - count) // loopCount
        multi = max(0, total) * loop

        ci = ps[ci] - 1

        currentV = cs[ci]
        currentSum += currentV

        answer = max(answer, multi + currentSum)
        if ci == i:
            break

print(answer)