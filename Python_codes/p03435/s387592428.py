import numpy as np
C= [[0] * 3 for i in range(3)]
for i in range(3):
  C[i]=list(map(int, input().split()))
C=np.array(C)
answer='Yes'
 
S=C.sum()
trace=np.diag(C).sum()
S_row0=C[0,:].sum()
S_row1=C[1,:].sum()
S_row2=C[2,:].sum()

S_col0=C[:,0].sum()
S_col1=C[:,1].sum()
S_col2=C[:,2].sum()

if S != 3*trace:
  answer = 'No'
elif S_row0-3*C[0,0] != trace-S_col0:
  answer = 'No'
elif S_row1-3*C[1,0] != trace-S_col0:
  answer = 'No'



print(answer)