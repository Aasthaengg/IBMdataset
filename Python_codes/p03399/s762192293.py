a,b,c,d = [int(input()) for _ in range(4)]
x = [a,b]
y = [c,d]

x.sort()
y.sort()

print(x[0]+y[0])