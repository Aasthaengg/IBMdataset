from scipy.spatial.distance import cdist
import numpy as np
#%%
n, m = map(int, input().split())

st = [list(map(int, input().split())) for _ in range(n)]
cp = [list(map(int, input().split())) for _ in range(m)]
#%%

# for s in st:
#     print(cityblock(s, np.array(cp)))
cd = cdist(st, cp, 'cityblock')
idx = np.argmin(cd, axis=1)
for i in idx:
    print(i+1)