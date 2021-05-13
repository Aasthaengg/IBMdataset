from math import log2, ceil

a, b, c = map(int, input().split())
k = int(input())
# n >= log2((a+1)/b)
bi = ceil(log2((a+1) / b))
bi = max(bi, 0)
b *= pow(2, bi)
ci = ceil(log2((b+1) / c))
ci = max(ci, 0)
if bi + ci <= k:
    print("Yes")
else:
    print("No")