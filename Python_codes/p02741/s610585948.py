arr = [0,1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
k = int(input())
for i in range(0, len(arr)):
    if i == k:
        print(arr[k])

