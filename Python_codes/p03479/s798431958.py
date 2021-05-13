X, Y = map(int, input().split())

max = 0
array = []
A = X
while (True):
    if A <= Y:
        array.append(A)
        A = A * 2
    else:
        break
if len(array) > max:
    max = len(array)
print(max)
