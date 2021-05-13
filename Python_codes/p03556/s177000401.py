import math

N = int(input())

for n in range(N):
    num = N - n
    sqrt_num = math.sqrt(num)
    
    if (int(sqrt_num) == sqrt_num):
        print(num)
        break