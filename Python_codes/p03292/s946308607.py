A = list(map(int, input().split()))

sm = 0
num1 = A.pop(A.index(min(A)))
num2 = A.pop(A.index(min(A)))
num3 = A.pop(A.index(min(A)))

sm += abs(num2 - num1)
sm += abs(num3 - num2)

print(sm)
