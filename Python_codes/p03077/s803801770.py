import math
n = int(input())
abc = sorted([int(input()) for _ in range(5)])
print(4+math.ceil(n/abc[0]))