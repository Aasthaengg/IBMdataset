import numpy as np 
N, M = input().split()
N = int(N)
M = int(M)
xs = []

for i in range(N):
    # select M
    x = np.array(input().split()).astype(np.int64)
    xs.append(x)
results = []
import itertools
for k in itertools.product((1,-1),(1,-1),(1,-1)):
    calcs = []
    for x in xs:
        calcs.append(k[0]*x[0]+k[1]*x[1]+k[2]*x[2])
    results.append(np.sort(calcs)[-M:].sum())
if M==0:
    print(0)
else:
    print(max(results))