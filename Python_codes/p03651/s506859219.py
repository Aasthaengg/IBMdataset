n,k=map(int,input().split())
A=list(map(int,input().split()))
yes="POSSIBLE" ; no="IMPOSSIBLE"
import numpy as np
q= np.gcd.reduce(A)
if k%q==0 and max(A)>=k:
    print(yes)
else:
    print(no)