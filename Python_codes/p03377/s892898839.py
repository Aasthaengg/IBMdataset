arr = input().split()
arr = list(map(int, arr))
a = arr[0]
b = arr[1]
x = arr[2]

if a <= x and x <= a+b:
    print('YES')
else:
    print('NO')
