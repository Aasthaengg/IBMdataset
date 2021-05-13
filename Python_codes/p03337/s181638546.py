arr = input().split()
arr = list(map(int, arr))

a = arr[0]
b = arr[1]


print(max(a+b,a-b,a*b))
