# coding: utf-8

N = int(raw_input())

dataList = []
for i in range(N):
    list = map(int, raw_input().split())
    dataList.append(list)

# find max number
for i in range(len(dataList)):
    idx = dataList[i].index(max(dataList[i]))
    lar = dataList[i][idx]
    del dataList[i][idx]
    if lar**2 == dataList[i][0] ** 2 + dataList[i][1]**2:
        print "YES"
    else:
        print "NO"