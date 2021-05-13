n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
for i in range(k, n):
    if arr[i] > arr[i-k]:
        print("Yes")
    else:
        print("No")