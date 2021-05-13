import numpy as np

N = int(input())
a_str = input().split()
a = np.zeros(N)

for i in range(N):
  a[i] = int(a_str[i])

mu = np.average(a)
diff = a - mu
abs_diff = np.abs(diff)

min = np.amin(abs_diff)
index = np.where(abs_diff == min)

print(index[0][0])