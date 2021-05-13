import math
n = int(input())
x = [int(i) for i in input().split()]
y = [int(j) for j in input().split()]
Manhattan = sum([abs(x[m]-y[m]) for m in range(n)])
Euclidean = math.sqrt(sum([(x[e]-y[e])**2 for e in range(n)]))
p_3 = (sum([(abs(x[c]-y[c]))**3 for c in range(n)]))**(1/3)
Chebyshev = max([abs(x[m]-y[m]) for m in range(n)])
print(Manhattan)
print(Euclidean)
print(p_3)
print(Chebyshev)
