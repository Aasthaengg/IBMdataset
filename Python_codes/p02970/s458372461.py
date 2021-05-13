#B
import math

n, d = map(int, input().split())

eye_range = d * 2 + 1
ans = n / eye_range
print(math.ceil(ans))