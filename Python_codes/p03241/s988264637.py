import numpy as np

n,m = map(int,input().split())
ans = 0
tmp = int(m/n)
for i in range(1,int(np.sqrt(m)+1)):
    if m%i == 0:
        if (ans < i) and(i <= tmp):
            ans = i
        tmp2 = m//i
        if (ans < tmp2) and(tmp2 <= tmp):
            ans = tmp2
print(ans)