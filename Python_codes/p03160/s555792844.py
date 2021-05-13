import math

# N = 4
# ARR = [10, 30, 40, 20]


N = int(input())
ARR = list(map(int, input().split()))

def calculate(n, arr):
    result = [math.inf for i in range(n)]

    result[0] = 0
    result[1] = abs(arr[1]-arr[0])


    for i in range(2,n):
        a1 = abs(arr[i] - arr[i-2]) + result[i-2]
        a2 = abs(arr[i] - arr[i-1]) + result[i-1]

        result[i] = min(a1,a2)


    print(result[-1])




calculate(N, ARR)
