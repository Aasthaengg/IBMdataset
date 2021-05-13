import numpy as np
n = int(input())
a = [int(i) for i in input().split()]
def div2(t):
    count = 0
    while t % 2 == 0:
        count += 1
        t //= 2
    return count
b = np.array([div2(i) for i in a])
odd = len(b[b == 0])
four = len(b[b >= 2])
if odd == 0:
    print('Yes')
elif odd == n:
    print('No')
elif odd <= four or ((odd == four + 1) and (odd + four) == n):
    print('Yes')
else:
    print('No')