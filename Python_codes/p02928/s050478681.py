from collections import defaultdict
 
n,k = map(int,input().split())
a = list(map(int,input().split()))
mod = 10**9 + 7
d = defaultdict(int)
 
inner = 0
for i in range(n):
    d[a[i]] += 1
    for j in range(i+1,n):
        if a[i] > a[j]:
            inner += 1
 
t = 0
for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            t += 1
 
x = ((t)*(k)*(k-1)//2)%mod
y = (inner*k)%mod
print(int((x+y)%mod))