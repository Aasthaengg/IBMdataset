import math
N = int(input())
ARR = [int(s) for s in input().split(" ")]
ARR.insert(0,0)
ARR.append(0)


def calculate(arr):
    S = 0
    for i in range(len(arr)-1):
        S = S + int(math.fabs(arr[i+1]-arr[i]))

    for i in range(1,len(arr)-1):
        print(int(S + math.fabs(arr[i-1]-arr[i+1]) - (math.fabs(arr[i-1]-arr[i]) + math.fabs(arr[i]-arr[i+1]))))



calculate(ARR)
