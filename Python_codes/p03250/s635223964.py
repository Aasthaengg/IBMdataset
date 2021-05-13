arr = list(map(int, input().split()))

arr.sort()

A = int(str(arr[2])+str(arr[1]))

B = int(arr[0])

print( A + B )