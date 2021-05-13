import math

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

d = [0 for _ in range(n)]
for i in range(n):
    d[i] = pow(math.fabs(x[i]-y[i]), 1)
D_1 = pow(sum(d), 1/1)

for i in range(n):
    d[i] = pow(math.fabs(x[i]-y[i]), 2)
D_2 = pow(sum(d), 1/2)

for i in range(n):
    d[i] = pow(math.fabs(x[i]-y[i]), 3)
D_3 = pow(sum(d), 1/3)

for i in range(n):
    d[i] = math.fabs(x[i]-y[i])
D_inf = max(d)

print(D_1)
print(D_2)
print(D_3)
print(D_inf)