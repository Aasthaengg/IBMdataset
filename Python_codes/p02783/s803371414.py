import math
H, A = map(int, input().split())
if H >= A:
    print(math.ceil(H / A))
elif H < A:
    print(1)