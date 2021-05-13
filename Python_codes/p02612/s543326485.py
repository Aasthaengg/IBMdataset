def solver(N):
    for i in range(1,11):
        charge = 1000 * i - N
        if charge >= 0 and charge < 1000:
            return charge

print(solver(int(input())))