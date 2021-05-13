x = input()
a, b, c = [int(z) for z in x.split()]
n = 0
for m in range(a, b+1):
    if c % m == 0:
        n += 1
print(n)