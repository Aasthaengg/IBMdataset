arr = []

A, B, C = list(map(int, input().split()))

arr.append(A)
arr.append(B)
arr.append(C)
arr = sorted(arr)

print(int(arr[0]*arr[1]*0.5))