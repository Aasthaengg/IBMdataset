import numpy as np

#A = list(map(int,input().split()))

N,D  = map(int,input().split())

ans = 0

for i in range(N):
    x,y = map(int,input().split())
    if x**2 + y**2 <= D**2:
        ans +=1

print(ans)