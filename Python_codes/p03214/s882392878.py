N=int(input())
a=list(map(int,input().split()))

ave_a=sum(a)/len(a)
import numpy as np
a=np.array(a)
de_a=abs(a-ave_a)
print(np.argmin(de_a))