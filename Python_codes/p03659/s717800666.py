import math

n = int(input())
a = list(map(int, input().split()))

m = 10**10
x = 0
X = sum(a)

for i in range(n):
    x += a[i]
    if i+1 < n:
        m = min(m, abs(X-2*x))

print(m)
