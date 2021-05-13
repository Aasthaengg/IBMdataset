import numpy as np
import sys
import distutils.util

h, w, k = (int(x) for x in input().split())
count = 0
map = ''
for i in range(h):
    map += sys.stdin.readline().replace('\n','')
map2 = [True]*len(map)
for i in range(len(map)):
    if map[i]=='.': map2[i]=False
map2 = np.array(map2, dtype=bool).reshape((h, w))

for i in range(2**h):
    tmp = bin(i)[2:]
    tmp = '0'*(h-len(tmp)) + tmp
    a = list((bool(distutils.util.strtobool(tmp[i]))
              for i in range(len(tmp))))
    tmp = np.array(a*w).reshape(w, h).transpose()
    for j in range(2**w):
        tmp2 = bin(j)[2:]
        tmp2 = '0'*(w-len(tmp2)) + tmp2
        b = list((bool(distutils.util.strtobool(tmp2[i]))
                  for i in range(len(tmp2))))
        tmp2 = np.array(b*h).reshape(h, w)
        if sum(sum(list(tmp & tmp2 & map2)))==k: count+=1

print (count)
