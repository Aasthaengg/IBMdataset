line = input()
X,Y = [int(n) for n in line.split()]

a,b,c = [X+Y, X-Y, X*Y]

res = max(a,b,c)

print(res)
