import math

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(sum([math.fabs((x[i] - y[i])) for i in range(n)]))
print(sum([math.fabs((x[i] - y[i]))**2 for i in range(n)])**(1/2))
print(sum([math.fabs((x[i] - y[i]))**3 for i in range(n)])**(1/3))
print(max([math.fabs((x[i] - y[i]))for i in range(n)]))