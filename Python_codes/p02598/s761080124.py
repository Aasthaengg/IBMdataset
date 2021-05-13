import math
def is_lt_or_e_K(k, x, a):
    if k >= sum([math.ceil(i / x) - 1 for i in a]):
        return True
    else:
        return False 
n, k = map(int, input().split())
a = list(map(int, input().split()))
high = max(a)
low = 0
while 1:
    if high - low < 2:
        break
    x = (high + low) // 2
    if is_lt_or_e_K(k, x, a):
        high = x
    else:
        low = x
print(high)
