import numpy as np
s = input()
ns = np.array(list(s))
n1 = ns[::2]
n2 = ns[1::2]
if not 'L' in n1 and not 'R' in n2:
    print('Yes')
else:
    print('No')