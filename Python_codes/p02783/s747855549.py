import math
H,A = map(int,input().split())
print(1 if H < A else math.ceil(H/A))