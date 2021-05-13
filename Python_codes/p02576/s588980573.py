import math

input_list = [int(num) for num in input().split()]

N = input_list[0]
X = input_list[1]
T = input_list[2]

ans = math.ceil(N/X)*T

print(ans)
