import numpy as np
n = int(input())
a_list = np.array(list(map(int, input().split())))

counter = 0
while True:
    if np.sum(a_list % 2) > 0:
        break
    counter += 1
    a_list = a_list / 2
print(counter)
