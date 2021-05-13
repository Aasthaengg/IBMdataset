arr = input().split()
arr = list(map(int,arr))
a = arr[0]
b = arr[1]
if a + b < 10:
    print(a+b)
else:
    print('error')
