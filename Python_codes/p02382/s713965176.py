import math
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
ab = [math.fabs(x[i]-y[i]) for i in range(n)]
p_1, p_2, p_3 = 0, 0, 0
for i in range(n):
    p_1 += ab[i]
for i in range(n):
    p_2 += ab[i]**2
p_2 = math.sqrt(p_2)
for i in range(n):
    p_3 += ab[i]**3
p_3 = p_3**(1/3)
p_inf = max(ab)
print(p_1)
print(p_2)
print(p_3)
print(p_inf)
