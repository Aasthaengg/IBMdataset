# B - Five Dishes
import numpy as np
n=[]
for i in range(5):
    t = int(input())
    n.append(t)
n = np.array(n)
dl = [0]
s = np.ceil(n/10)*10

if max(n%10)==0:
    print(int(np.sum(s)))
    exit()
m = [e for e in n%10 if e not in dl]
print(int(np.sum(s)-(10-min(m))))