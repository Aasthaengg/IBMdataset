import math
n = int(input())
nn = 1
xl = []
yl = []
ll = 0
for i in range(n):
    x,y = map(int, input().split())
    xl.append(x)
    yl.append(y)
 
j = 0
while j < n-1:
    k = j+1
    while k <= n-1:
        ll += math.sqrt((xl[j]-xl[k])**2 + (yl[j] - yl[k])**2)
        k += 1
    j += 1
 
print(ll*2/n)