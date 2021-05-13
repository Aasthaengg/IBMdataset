na = int(input())
nb = int(input())
nc = int(input())
xx = int(input())
counter = 0
for aa in range(na+1):
    for bb in range(nb+1):
        residue = xx-500*aa-100*bb
        if residue >= 0 and residue / 50 <= nc:
            counter += 1
print(counter)