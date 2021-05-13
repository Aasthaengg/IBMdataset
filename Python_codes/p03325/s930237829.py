import numpy as np
s = list(map(int, input().split()))
n=s[0]
s = list(map(int, input().split()))
ans=0
for i in s:
    while i%2==0:
        i/=2
        ans+=1
print(ans)
