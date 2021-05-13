import numpy as np

h, n = map(int, input().split())
attack = list(map(int, input().split()))

attack_arr = np.array(attack)

if attack_arr.sum() >= h:
    print('Yes')
else:
    print('No')