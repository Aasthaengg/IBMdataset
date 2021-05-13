a, z, mult = input().split()

a, z, mult = int(a), int(z), int(mult)

cont = 0
for i in range(a, z+1):
    if i%mult == 0:
        cont += 1;
        
print(cont)