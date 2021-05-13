n = int(input())
X = [int(i) for i in input().split()]
Y = [int(i) for i in input().split()]
a = [abs(X[i] - Y[i]) for i in range(n)]
print(sum(a))
print((sum([x**2 for x in a]))**0.5)
print((sum([x**3 for x in a]))**(1/3))
print(max(a))