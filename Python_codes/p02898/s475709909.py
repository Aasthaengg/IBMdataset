import numpy as np

N,K=map(int,input().split())
h=list(map(int,input().split()))
# N,K=4,150
# h=[150, 140, 100, 200]

harry=np.array(h)
ans=np.count_nonzero(harry>=K)

print(ans)


# import sys
# print(sys.version_info)