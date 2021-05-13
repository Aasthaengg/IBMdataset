import numpy as np

s = input()
s_list = np.array([1 if s[i] == "p" else 0 for i in range(len(s))])
myhand = np.array([0 if i % 2 == 0 else 1 for i in range(len(s))])
print(np.sum(myhand - s_list))
