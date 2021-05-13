N,A,B = map(int,input().split())
ARR = list(map(int,input().split()))
def calculate(n,a,b,arr):

    result = 0
    for i in range(1,n):
        result += min(B,(arr[i] - arr[i-1]) * A)

    print(result)

calculate(N,A,B,ARR)