import numpy as np
A,B,C,D = map(int,input().split())
E = np.lcm(C,D)
print(1+B-A-B//C+(A-1)//C-B//D+(A-1)//D+B//E-(A-1)//E)