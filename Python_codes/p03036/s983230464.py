r, d, x0 = map(int, input().split())
x = [x0]
for i in range(10):
    x.append(r*x[-1] - d)
print(*x[1:], sep='\n')