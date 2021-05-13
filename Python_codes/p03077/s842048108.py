import math

N=int(input())
arr=[int(input()) for i in range(5)]
mm=arr.index(min(arr))


time=4+math.ceil(N/arr[mm])

print(time)
