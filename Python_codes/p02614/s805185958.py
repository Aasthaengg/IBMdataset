import sys
import numpy as np
import itertools
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

H,W,K=map(int,readline().split())
C=np.array(list(map(str,read().rstrip().decode().split())))
ans=0
for paint_H in itertools.product([0,1], repeat=H):
  for paint_W in itertools.product([0,1], repeat=W):
    cnt=0
    for i in range(H):
      for j in range(W):
        if paint_H[i]==0 and paint_W[j]==0 and C[i][j]=="#":
          cnt+=1
    if cnt==K:
      ans+=1
print(ans)