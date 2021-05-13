import math
n=int(input())
k=int(input())
out=1
for a in range(n):
    if out<=k:
        out*=2
    else:
        out+=k
print(out)