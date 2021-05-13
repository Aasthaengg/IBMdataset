import sys
import numpy as np
input = sys.stdin.readline

n=int(input())
v=np.array(list(map(int,input().split())))
c=np.array(list(map(int,input().split())))
s = (v-c)
ans =0
for ss in s:
    ans += ss*(ss>0)
print(ans)
