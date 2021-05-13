import numpy as np
n=int(input())
x1=list(map(int,input().split()))
ans=1000000000000000000000
for i in np.arange(1,101):
    hp=0
    for j in x1:
        hp+=(j-i)*(j-i)
    if hp<=ans:
        ans=hp
print(ans)