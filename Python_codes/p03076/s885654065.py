from itertools import permutations
import numpy as np

lis = [int(input()) for i in range(5)]
total = np.inf
now = 0
for a,b,c,d,e in permutations(lis,5):
    now = ((a-1)//10+1)*10+((b-1)//10+1)*10+((c-1)//10+1)*10+((d-1)//10+1)*10+e
    total = min(total,now)
    #print(now)
    #print(total)

print(total)