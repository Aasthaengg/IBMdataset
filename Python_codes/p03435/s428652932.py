import numpy as np

c = [list(map(int,input().split())) for i in range(3)]
c = np.array(c)
flg = True

for i in range(2):
    if not c[0,i]-c[0,i+1] == c[1,i]-c[1,i+1] == c[2,i]-c[2,i+1]:
        flg = False
        break
    if not c[i,0]-c[i+1,0] == c[i,1]-c[i+1,1] == c[i,2]-c[i+1,2]:
        flg = False
        break
print('Yes') if flg else print('No')