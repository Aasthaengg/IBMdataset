line = input()
a, b, c = [int(n) for n in line.split()]
soma=0
for a in range(a, c+1, a):
    soma=b+soma
print(soma)