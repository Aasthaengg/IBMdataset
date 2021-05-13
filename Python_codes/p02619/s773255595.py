import numpy as np

D = int(input()) 
c = list(map(int,input().split())) 
s = [list(map(int,input().split())) for i in range(D)]
t = [int(input().strip()) for _ in range(D)]

last = []
for i in range(26):
    last.append(0)

last = np.array(last)
ans = 0
for i in range(D):
    last[t[i]-1] = i+1
    dec = c * (i+1-last)
    #ans = ans + s[i][t[i]] 
    ans = ans + s[i][t[i]-1] - sum(dec)
    print(ans)