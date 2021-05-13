import numpy as np
N = int(input())
a = np.array(list(map(int,input().split())))

xor = 0
for i in a:
    xor ^=i

for i in a:
    print(xor^i)