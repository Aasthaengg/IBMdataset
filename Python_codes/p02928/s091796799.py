import math
n,k = map(int,input().split())
a = list(map(int,input().split()))
lim = int((1e+9)+7)
right = [0 for _ in range(n)]
left = [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[j] < a[i]:
            if i < j:
                right[i] += 1
            else:
                left[i] += 1
ans = 0
def c(g):
    re = g*(g-1)//2
    return re

for i in range(n):
    ans = (ans - (left[i]*k) + ((right[i]+left[i])*c(k+1)))%lim
print(ans)