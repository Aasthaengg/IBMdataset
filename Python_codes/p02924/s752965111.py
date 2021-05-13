from math import ceil
N = int(input())
n = N -1
if n == 1:
    ans = 1
elif n%2 != 0:
    ans = (1+n)*(n//2) + ceil(n/2)
else:
    ans = (1+n)*(n//2)
print(ans)