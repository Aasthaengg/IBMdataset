import math
n = int(input())
if (n-1)%2 == 0:
    a = int((n-1)/2)
    ans = n*a
else:
    ans = n * math.floor((n-1)/2) + math.ceil((n-1)/2)

print(int(ans))