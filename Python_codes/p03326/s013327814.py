import numpy as np
import itertools

n,m = map(int, input().split())
XYZ = [list(map(int, input().split())) for _ in range(n)]
X = np.array([xyz[0] for xyz in XYZ])
Y = np.array([xyz[1] for xyz in XYZ])
Z = np.array([xyz[2] for xyz in XYZ])

ans_list = []

for i,j,k in itertools.product([1,-1], repeat=3):
  temp_ans = i*X+j*Y+k*Z
  ans_list.append(sum(np.sort(temp_ans)[::-1][:m]))
  
print(max(ans_list))