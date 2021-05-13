import sys
n = int(input())
print(0)
s = input()
if s == "Vacant":
    sys.exit()
lb, ub = 0, n
ls, us = s, s
while True:
    mid = (lb + ub) // 2
    print(mid)
    mis = input()
    if mis == "Vacant":
        sys.exit()
    if (ls == mis) ^ ((mid - lb) & 1):
        lb = mid
        ls = mis
    else:
        ub = mid
        us = mis
