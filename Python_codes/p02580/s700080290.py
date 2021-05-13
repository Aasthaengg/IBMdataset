H, W, M = map(int,input().split())
ARR = []

for i in range(M):
    ARR.append(list(map(int,input().split())))

def calculate(h, w, m, arr):
    points = set()



    rowSum = [0 for i in range(h)]
    columnSum = [0 for i in range(w)]

    for ar in arr:
        points.add((ar[0]-1, ar[1]-1))
        rowSum[ar[0]-1] += 1
        columnSum[ar[1]-1] += 1

    maxRowSum = max(rowSum)
    maxColumnSum = max(columnSum)


    a0 = []

    for i in range(len(rowSum)):
        if rowSum[i] == maxRowSum:
            a0.append(i)

    a1 = []
    for i in range(len(columnSum)):
        if columnSum[i] == maxColumnSum:
            a1.append(i)

    result = 0
    for hIndex in a0:
        for wIndex in a1:

            if (hIndex,wIndex) in points:
                result = max(result, maxRowSum + maxColumnSum - 1)
            else:
                result = max(result, maxRowSum + maxColumnSum)
                print(result)
                exit()

    print(result)


calculate(H, W, M, ARR)
