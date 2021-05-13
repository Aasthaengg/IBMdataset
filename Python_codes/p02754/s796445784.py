N, A, B = map(int, input().split())

AB = A + B
NumABalls = 0

NumABalls = N//AB * A
M = N%AB

if A - M >= 0:
  NumABalls += M
else:
  NumABalls += A

print(NumABalls)