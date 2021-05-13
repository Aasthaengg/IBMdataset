import math

def cal(n):
    if n == 1:
        return 0
    else:
        return (n-1)+cal(n-1)
n = int(input())
x = [None]*n
y = [None]*n
total = 0
for i in range(n):
    x[i], y[i] = map(int, input().split())

for i in range(n):
    for j in range(n):
        total += math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
total = total/2
ans = total*(n-1)/cal(n)

print(ans)