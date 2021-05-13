arr = input().split()
arr = list(map(int,arr))

if arr[0] + arr[1] == arr[2] + arr[3]:
    print('Balanced')
elif arr[0] + arr[1] > arr[2] + arr[3]:
    print('Left')
else:
    print('Right')
