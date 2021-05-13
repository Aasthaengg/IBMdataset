from math import floor

H = int(input())

c = 1
res = 0
while H > 0:
    H = floor(H/2)
    res += c
    c <<= 1

print(res)