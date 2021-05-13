import math

input = map(float, raw_input().split(" "))
print math.pow((input[0] - input[2]) ** 2 + (input[1] - input[3]) ** 2, 0.5)