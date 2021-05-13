import numpy as np
a = np.array(input().split(), dtype='int')
b = np.array(input().split(), dtype='int') - a
c = np.array(input().split(), dtype='int') - a

if np.all(b == b[0]) and np.all(c == c[0]):
    print('Yes')
else:
    print('No')