arr = input().split()
arr = list(map(int,arr))
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a <= c and c <= b:
    print('Yes')
else:
    print('No')
