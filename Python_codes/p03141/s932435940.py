import numpy as np
n = int(input())
al = np.zeros(n)
bl = np.zeros(n)
for i in range (n):
    al[i],bl[i] = map(int,input().split())
id = [*range(n)]
s=al+bl
id = sorted(id, key=lambda i: -s[i])
s=np.sort(s)
ans = 0 
for i in range(n):
    if i%2==0:
        ans+=al[id[i]]
    else:
        ans-=bl[id[i]]
print(int(ans))