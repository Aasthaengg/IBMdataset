O = input()
E = input()
password = []
for i in range(max(len(O), len(E))):
    if i <= len(O) - 1:
        password.append(O[i])
    if i <= len(E) - 1:
        password.append(E[i])
print(*password, sep='')