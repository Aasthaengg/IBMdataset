a,b = map(int,input().split())
x = []
for i in range(b):
    x.append(1)
    a = a - 1
for i in range(a):
    x[0] = x[0] + 1
x.sort()
print(abs(x[0] - x[len(x) - 1]))