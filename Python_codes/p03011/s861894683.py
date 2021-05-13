import sys
import numpy as np
import itertools

p,q,r = input().split()
p = int(p)
q = int(q)
r = int(r)
dest_min = p + q + r
dest = np.array(list(itertools.combinations([p,q,r],2)))


for dest_sample in dest:
    dest_min = min(dest_min, np.sum(dest_sample))

print(dest_min)