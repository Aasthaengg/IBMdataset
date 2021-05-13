N = int(input())
arr = [int(input()) for _ in range(N)]
arr2 = sorted(arr)
max1 = arr2[-1]
max2 = arr2[-2]
for i in range(N):
    if arr[i] == max1:
        print(max2)
    else:
        print(max1)