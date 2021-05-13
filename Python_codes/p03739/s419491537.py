import numpy as np
n = int(input())
a = list(map(int, input().split()))

s = 0
ans1 = 0
ans2 = 0

for i in range(len(a)):
    s += a[i]
    if(i%2 == 0):
        if(np.sign(s) != 1):
            ans1 += abs(1 - s)
            s = 1
    else:
        if(np.sign(s) != -1):
            ans1 += abs(-1-s)
            s = -1
s = 0
for i in range(len(a)):
    s += a[i]
    if(i%2==0):
        if(np.sign(s) != -1):
            ans2 += abs(-1-s)
            s = -1
    else:
        if(np.sign(s) != 1):
            ans2 += abs(1-s)
            s = 1
print(min(ans1, ans2))