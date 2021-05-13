import math
n = int(input())
result = math.ceil(n / 1.08)
print(result) if math.floor(result * 1.08) == n else print(":(")