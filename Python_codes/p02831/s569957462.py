import math
A, B = list(map(lambda x: int(x), input().split(" ")))

print(int(A * B / math.gcd(A, B)))