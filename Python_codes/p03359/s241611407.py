arr = input().split()
arr = list(map(int,arr))

a = arr[0]
b = arr[1]

if b < a:
    print(a-1)
else:
    print(a)
