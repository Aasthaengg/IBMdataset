n = int(input())
a_l = list(map(int, input().split()))
import numpy as np
ave_a = np.mean(a_l)
a_l2 = [ (i, abs(j-ave_a)) for i,j in enumerate(a_l) ]
a_l3 = sorted(a_l2, key=lambda x: x[1])
print(a_l3[0][0])