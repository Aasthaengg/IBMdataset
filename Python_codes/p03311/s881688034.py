import math
n=int(input())
res = [0]*n
A=[int(i) for i in input().split()]
for i in range(n):
    res[i]=(A[i]-(i+1))
res.sort()

if n%2==1:
    ans = sum([abs(i-res[n//2]) for i in res])
else:
    b0 = (res[n//2-1]+res[n//2])//2
    b1 = (res[n//2-1]+res[n//2])
    ans = min(sum([abs(a-b0) for a in res]), sum([abs(a-b1) for a in res]))
print(ans)
