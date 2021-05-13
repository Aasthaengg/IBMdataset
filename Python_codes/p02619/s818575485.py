import numpy as np
D = int(input())
c = np.array(list(map(int,input().split())))
s = np.array([list(map(int,input().split())) for _ in range(D)])
t = np.array([int(input())-1 for _ in range(D)])

last = np.full(26,-1)

S = 0
score = 0;
for i,v in enumerate(t):
    S += s[i][v]
    last[v] = i
    tmp =c*(i - last)
    S -= sum(tmp) 
    score +=max(10**6+S,0)
    print(S)
