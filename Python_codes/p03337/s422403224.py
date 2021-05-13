a,b = map(int,input().split())
x = []
x.append(a + b)
x.append(a * b)
x.append(a - b)
x.sort()
print(x[2])