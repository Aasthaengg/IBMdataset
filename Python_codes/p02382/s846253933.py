from math import fabs, sqrt

n = int(input())
x = list(map(float, input().strip().split()))
y = list(map(float, input().strip().split()))

sum1 = 0
sum2 = 0
sum3 = 0
pil = []

for i in range(n):
    sum1 += fabs(x[i] - y[i])
    sum2 += fabs(x[i] - y[i]) ** 2
    sum3 += fabs(x[i] - y[i]) ** 3
    pil.append(fabs(x[i] - y[i]))

pil = sorted(pil)
p1 = sum1
p2 = sqrt(sum2)
p3 = sum3 ** (1 / 3)
pi = pil[n-1]

print(round(p1, 8))
print(round(p2, 8))
print(round(p3, 8))
print(round(pi, 8))
