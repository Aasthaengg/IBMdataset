import numpy as np

n = int(input())

l = list( map(int, input().split()) )

x = np.array(l)

avg = x.mean()

min = np.argmin(np.abs(x - avg))

print(min)