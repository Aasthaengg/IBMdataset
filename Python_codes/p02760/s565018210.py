# ABC157 B
import numpy as np
a = [[input().split() for l in range(3)]]
a = np.ravel(a)
n = int(input())
b = [input() for i in range(n)]
ans = 'No'

def check(a,b):
    return set(a).issubset(b)

for i in range(3):
    if check(a[i*3:(i*3)+3],b) or check(a[i:i+7:3],b) or check(a[0:9:4],b) or check(a[2:7:2],b):
        ans = 'Yes'

print(ans)