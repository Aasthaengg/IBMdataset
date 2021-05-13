N, M, X, Y = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

is_war = True

import numpy as np

for Z in range(X+1, Y+1):
    if np.all(np.array(x_list) < Z) and np.all(np.array(y_list) >= Z):
        is_war = False
        break
    
if is_war:
    print("War")
else:
    print("No War")