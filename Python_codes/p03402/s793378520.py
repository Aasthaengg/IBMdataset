import numpy as np
a,b = map(int, input().split())

x=np.array([['.']*100]*100,dtype=str)

x[:,:50]='#'

v1=(a-1)//20
v2=(a-1)-v1*20
w1=(b-1)//20
w2=(b-1)-w1*20

for i in range(v1):
    x[2*i+1,1:40:2]='.'

x[-1,1:2*v2:2]='.'

for i in range(w1):
    x[2*i+1,51:90:2]='#'
x[-1,51:50+w2*2:2]='#'
print(100,100)
for i in range(100):
    print(''.join(x[i]))