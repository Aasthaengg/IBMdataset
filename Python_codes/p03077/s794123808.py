import math
N = int(input())
root_list = []
for i in range(5):
    root_list.append(int(input()))
min_root=min(root_list)
print(math.ceil(N/min_root)+4)