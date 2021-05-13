import numpy as np 

s_ = input()
s = np.array([int(s_[i]) for i in range(len(s_))])
k = 0
for n in s:
    k += n
if k % 9 ==0:
    print("Yes")
else:
    print("No")