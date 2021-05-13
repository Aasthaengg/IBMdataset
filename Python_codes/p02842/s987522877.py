import math

N = int(input())

result = math.ceil(N / 1.08)

comfirm_result = int(result * 1.08)

if comfirm_result == N:
    print(result)
else:
    print(':(')