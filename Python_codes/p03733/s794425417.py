import os

N,T = (int(x) for x in input().split())
t = [int(i) for i in input().split()]

ans = 0
sum = 0
for i in range(N-1):
    if t[i+1]-t[i]>=T:
        ans += T
    else:
        ans += t[i+1]-t[i]
print(ans+T)
