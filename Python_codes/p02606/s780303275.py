L, R, d = [int(x) for x in input().split()]
comp = 0
for el in range(L, R+1):
    if el % d == 0:
        comp += 1

print(comp)