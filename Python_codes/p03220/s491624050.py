n = int(input())
t, a = map(int,input().split())
beta = 0.006
H = list(map(int,input().split()))
import numpy as np 
H = np.array(H) 
use = t - beta * H - a 
use = use**2 
pre_answer = min(use)
use = list(use) 
ans = 1 + use.index(pre_answer) 
print(ans)