import numpy as np
N, L = map(int,input().split())
AL = []
ans = 0

for i in range(1, N+1):
    Ap = L + i - 1
    AL.append(Ap)
tmp = sorted(np.abs(AL))[0] 

for i in range(1, N+1):
    App = L + i - 1
    if abs(App) != tmp:
        ans += App

print(ans)