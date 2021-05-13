O = list(str(input()))
E = list(str(input()))

list = []

if len(O)==len(E):
    for i in range(len(O)):
        list.append(O[i])
        list.append(E[i])

else:
    for i in range(len(E)):
        list.append(O[i])
        list.append(E[i])
    list.append(O[-1])

L="".join(list)
print(L)
