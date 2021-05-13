# coding: utf-8
timestamp = 1

stack = []
indata = []
visit = []      #?¨?????¨????
visitTime = []  #?¨???????????¨??????¨
lastTimeStack = []      #?¨?????????????????¨??????¨


def inputdata():
    global      visit
    global      indata
    global      visitTime

    n = int(input().rstrip())

    for i in range(n):
        visit.append(True)
        visitTime.append([0, 0])

        lst = [int(i) for i in input().rstrip().split(" ")]
        k = lst[1]
        v = []
        for j in range(k):
            v.append(lst[2 + j] - 1)
        indata.append(v)

def procV(n):
    global lastTimeStack
    global timestamp
    global visit
    global stack

    if visit[n]:
        stack.append(n)
        lastTimeStack.append(n)
        visitTime[n][0] = timestamp
        timestamp += 1
        visit[n] = False
    else:
        if visitTime[n][1] == 0:
            visitTime[n][1] = timestamp
            timestamp += 1

"""
main
"""
inputdata()
stack.append(0)             #?????????????´????push??????

while True:
    if len(stack) == 0:
        isNotVisit = True
        n = 0
        for i in visit:
            if i:
                isNotVisit = False
                stack.append(n)
                break
            n += 1
        if isNotVisit:
            break

    n = stack.pop()         #??????????????????pop??????
    procV(n)                #pop????????????????????????????????????

    #???????????¢???
    for i in reversed(indata[n]):
        if visit[i]:
            hasNotChildAdd = False
            stack.append(i)

i = 1
for val in visitTime:
    li = [i, val[0], val[1]]
    print(' '.join(map(str, li)))
    i += 1