import math

inputted = list(map(int, input().split()))
N = inputted[0]
D = inputted[1]

monitor = D * 2 + 1
answer = math.ceil(N / monitor)

print(answer)
