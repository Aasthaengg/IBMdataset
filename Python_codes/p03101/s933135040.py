import numpy as np
box_size = list(map(int, input().split())) 
fill_num = list(map(int, input().split())) 
 
box = np.array([[1]*box_size[1]]*box_size[0])
for r in range(fill_num[0]):
    box[r,:] = 0
for c in range(fill_num[1]):
    box[:,c] = 0
print(np.sum(box))