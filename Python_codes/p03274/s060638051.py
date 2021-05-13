n, k = map(int, input().split())
a = list(map(int, input().split()))
#from numpy import sign
#import numpy as np
out = float('Inf')
for i in range(0, n - k + 1):
    ans = abs(a[i] - a[i + k - 1]) + min(abs(a[i]), abs(a[i + k - 1]))
    out = min(out, ans)
print(out)