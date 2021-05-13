import numpy as np
n = int(input())
a = np.array(list(map(int, input().split())))
sub = np.array(list(range(n)))
b = sorted(a - sub)[n // 2]
print(sum(abs(a - (b + sub))))
