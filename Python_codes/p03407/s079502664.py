arr = input().split()
arr = list(map(int,arr))
if arr[0] + arr[1] >= arr[2]:
    print('Yes')
else:
    print('No')
