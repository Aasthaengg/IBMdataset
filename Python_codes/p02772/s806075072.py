import numpy as np
N = int(input())
a = np.array([a for a in map(int, input().split()) if a % 2 == 0])
b = (a % 3) * (a % 5)
print('APPROVED' if b.sum() == 0 else 'DENIED')
