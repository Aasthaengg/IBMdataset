O = input()
E = input()

password = []
for i in range(len(O)):
    password += [O[i]]
    if i == len(O) - 1:
        if i != len(E):
            password += [E[i]]
    else:
        password += [E[i]]
print(''.join(password))