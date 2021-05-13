import numpy as np

n = int(input())
a = list(map(int, input().split()))

a = np.array(a)
s = a.cumsum()
ans = abs(2*s - sum(a))


print(min(ans))