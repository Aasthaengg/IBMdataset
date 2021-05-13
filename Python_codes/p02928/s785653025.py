n, k = map(int, input().split())
a = list(map(int, input().split()))
from collections import Counter
c = Counter(a)
x = 0
for i in range(n-1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            x += 1
y = 0
mod = 10 ** 9 + 7
for i in range(n):
    for j in c.keys():
        if j < a[i]:
            y += c[j]
print((((y*k*(k-1)//2 ))+(k*x)%mod)%mod)