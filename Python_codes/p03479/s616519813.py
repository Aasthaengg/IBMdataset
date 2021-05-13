X, Y = map(int,input().split())

arr = []
arr.append(X)
while arr[-1] * 2 <= Y:
    arr.append(arr[-1] * 2)
print(len(arr))