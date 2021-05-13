N,W = map(int,input().split())
l0=[]
l1=[]
l2=[]
l3=[]
for i in range(N):
    w,v = map(int,input().split())
    if i == 0:
        w1 = w
    if w == w1:
        l0.append(v)
    elif w == w1+1:
        l1.append(v)
    elif w == w1+2:
        l2.append(v)
    elif w == w1+3:
        l3.append(v)

l0.sort()
l0.reverse()
l1.sort()
l1.reverse()
l2.sort()
l2.reverse()
l3.sort()
l3.reverse()
l0 = [0]+l0
l1 = [0]+l1
l2 = [0]+l2
l3 = [0]+l3
import numpy as np
l0 = np.cumsum(np.array(l0))
l1 = np.cumsum(np.array(l1))
l2 = np.cumsum(np.array(l2))
l3 = np.cumsum(np.array(l3))

ans = 0
for i in range(len(l0)):
    for j in range(len(l1)):
        for k in range(len(l2)):
            for l in range(len(l3)):
                if i*w1+j*(w1+1)+k*(w1+2)+l*(w1+3)<=W:
                    if ans < l0[i]+l1[j]+l2[k]+l3[l]:
                         ans = l0[i]+l1[j]+l2[k]+l3[l]

print(ans)