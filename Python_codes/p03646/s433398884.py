import numpy as np
k=int(input())
t=np.array([49+((k-1)//50+1)]*50)
for i in range(0 if k%50==0 else 50-k%50):
    k=np.argmax(t)
    t+=1
    t[k]-=50+1
print(50)
print(*t)