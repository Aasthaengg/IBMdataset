
import numpy as np
n = int(input())
vList = np.array(list(map(int, input().split())) )
cList = np.array(list(map(int, input().split())) )
dList = vList-cList
ret = np.nansum(dList[dList > 0])

print(ret)