import numpy as np
s = input()
a = ["a","b","c"]
b = np.zeros(len(a))
for i in range(len(s)):
    if s[i] in a:
        b[a.index(s[i])]+=1
if max(b)-min(b)<=1:
    print("YES")
else:
    print('NO')