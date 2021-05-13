import math

inputted = list(map(int, input().split()))
A = inputted[0]
P = inputted[1]

answer = math.floor((A * 3 + P) / 2)

print(answer)
