import numpy as np
D = int(input())
c = np.array(list(map(int,input().split())))
s = np.array([list(map(int,input().split())) for _ in range(D)])
t = np.array([int(input())-1 for _ in range(D)])

last = np.full(26,-1)

S = 0
score = 0;
for d in range(D):
    S += s[d][t[d]]
    last[t[d]] = d
    for i in range(26):
        S-=c[i]*(d - last[i])
    score +=max(10**6+S,0)
    print(S)
