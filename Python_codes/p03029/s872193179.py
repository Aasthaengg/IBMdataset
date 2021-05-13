import math

number = input().split(" ")
A = int(number[0])
P = int(number[1])
apple = (A * 3) + P
print(math.floor(apple / 2))