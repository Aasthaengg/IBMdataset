import numpy as np

n = int(input())
a = np.array(list(map(int,input().split())), dtype=int)
b = np.zeros(n, dtype=int)

for i in range(n-1, -1, -1):
    m = sum(b[i::i+1]) % 2
    b[i] = (a[i] + m) % 2
bsum =sum(b) 
if bsum == 0:
    print(bsum)
else:
    ans = np.where(b>0)[0] + 1
    ans = ans.astype('str')
    print(bsum)
    print(' '.join(ans))