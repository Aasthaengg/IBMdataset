import numpy as np
dishes = [int(input()) for _ in range(5)]
dishes = sorted(dishes, key=lambda x: x % 10)
minutes = 0
first = True
for i in dishes:
    if i % 10 == 0:
        minutes += i
    else:
        if first:
            minutes += i
            first = False
        else:
            minutes += int(np.ceil(i/10)*10)
print(minutes)