import math

lst = []
for i in range(6):
    lst.append(int(input()))
min_ = min(lst[1:])
print(math.ceil(lst[0] / min_) + 4)