arr = input().split()
arr = list(map(int,arr))
n = arr[0]
a = arr[1]
b = arr[2]

print(min(a*n,b))
