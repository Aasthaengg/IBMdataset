X, Y = map(int, input().split())
A = [X]

while A[-1] <= Y:
    A.append(A[-1]*2)

print(len(A)-1)
