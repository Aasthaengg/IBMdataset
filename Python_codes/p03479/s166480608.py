X, Y = map(int, input().split())

A = [X]
while True:
    if A[-1] * 2 <= Y:
        A.append(A[-1] * 2)
    else:
        break

print(len(A))