arr = input().split()
arr = list(map(int, arr))

if arr[0] <= 8 and arr[1] <= 8:
    print('Yay!')
else:
    print(':(')
