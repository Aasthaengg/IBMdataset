import math

n = int(raw_input())
X = map(float, raw_input().split(" "))
Y = map(float, raw_input().split(" "))

print(sum([math.fabs(X[i] - Y[i]) for i in range(n)]))
print(math.sqrt(sum([math.fabs(X[i] - Y[i])**2 for i in range(n)])))
print(math.pow(sum([math.fabs(X[i] - Y[i])**3 for i in range(n)]), (1.0/3.0)))
print(max([math.fabs(X[i] - Y[i]) for i in range(n)]))