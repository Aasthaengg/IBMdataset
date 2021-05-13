import numpy as np
n,k = map(int,input().split())
s = input()
lr_cnt = 0
rl_cnt = 0
mnt = 0
for i in range(len(s)-1):
    if s[i] == 'L' and s[i+1] == 'R':
        lr_cnt += 1
        
    if s[i] == 'R' and s[i+1] == 'L':
        rl_cnt += 1
mnt  = rl_cnt + lr_cnt+1
mnt = np.max([1,mnt-2*k])
if mnt == 1:
    print(n-1)
else:
    print(n-rl_cnt-lr_cnt+2*k-1)